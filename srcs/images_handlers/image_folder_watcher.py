import os
import io
import cv2
import time
import sqlite3
import numpy as np
from rembg import remove
import concurrent.futures
from PIL import Image
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


processing_images = set()  # To track actively processing images


def is_image_processed(image_path):
    """Check if the image path exists in the database."""
    folder = os.path.join(os.path.expanduser("~"), 'romao_database')
    db_path = os.path.join(folder, 'database.db')

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('SELECT image_path FROM images_paths WHERE image_path = ?', (image_path,))
    result = cursor.fetchone()
    conn.close()

    return result is not None


def update_processed_image_path(image_path):
    """Add the processed image path to the database."""
    folder = os.path.join(os.path.expanduser("~"), 'romao_database')
    db_path = os.path.join(folder, 'database.db')

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO images_paths (image_path)
        VALUES (?)
    ''', (image_path,))
    conn.commit()
    conn.close()


class ImageHandler(FileSystemEventHandler):
    """Handles image folder events for new or modified images."""

    def on_created(self, event):
        if event.is_directory or not event.src_path.lower().endswith(('.png', '.jpg', '.jpeg')):
            return

        # Collect multiple new images and process them concurrently
        if event.src_path not in processing_images:
            process_images_concurrently([event.src_path])


    def on_modified(self, event):
        if event.is_directory or not event.src_path.lower().endswith(('.png', '.jpg', '.jpeg')):
            return

        # Check if the image is being processed already
        if event.src_path in processing_images:
            return  # Skip if already processing

        process_image(event.src_path)


def wait_for_file_ready(image_path, timeout=10):
    """Wait until the file is accessible or timeout."""
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            with Image.open(image_path):
                return True
        except (IOError, FileNotFoundError):
            time.sleep(0.5)
    raise TimeoutError(f"File not ready after {timeout} seconds: {image_path}")

def crop_to_object(image: Image.Image) -> Image.Image:
    img = np.array(image.convert("RGBA"))
    alpha_channel = img[:, :, 3]  # Use the alpha channel to find contours
    _, thresh = cv2.threshold(alpha_channel, 1, 255, cv2.THRESH_BINARY)

    # Optional: Morphological operations to refine the mask
    kernel = np.ones((3, 3), np.uint8)
    thresh = cv2.dilate(cv2.erode(thresh, kernel, iterations=1), kernel, iterations=1)

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        x, y, w, h = cv2.boundingRect(max(contours, key=cv2.contourArea))
        cropped = img[y:y + h, x:x + w]
        return Image.fromarray(cropped)
    return image


def pad_to_square(image: Image.Image, size=100, fill=(255, 255, 255, 0)):
    """Resize the image to a square canvas with transparent padding."""
    width, height = image.size
    max_dim = max(width, height)
    new_img = Image.new("RGBA", (max_dim, max_dim), fill)  # Transparent background
    new_img.paste(image, ((max_dim - width) // 2, (max_dim - height) // 2), mask=image.split()[3])  # Use alpha channel as mask
    return new_img.resize((size, size), Image.Resampling.LANCZOS)

def calculate_scaled_dimensions(img, max_width, max_height):
    """Calculates the scaled width and height while preserving aspect ratio."""
    width, height = img.size

    # Calculate the scaling factor
    scale_factor = min(max_width / width, max_height / height)

    # Calculate new width and height
    scaled_width = int(width * scale_factor)
    scaled_height = int(height * scale_factor)

    return scaled_width, scaled_height, scale_factor


def process_images_concurrently(image_paths):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(process_image, image_paths)

def process_image(image_path):
    """Process the image in place."""
    global processing_images
    try:
        # Wait for the file to be ready
        wait_for_file_ready(image_path)

        if image_path in processing_images:
            return  # Already processing this image

        # Add the image to the processing set
        processing_images.add(image_path)

        # Check if file has already been processed
        if is_image_processed(image_path):
            return  # Skip reprocessing the image

        # Open and process the image
        img = Image.open(image_path)
        bg_removed_image = remove_background(img)
        scaled_width, scaled_height, _ = calculate_scaled_dimensions(bg_removed_image, 50, 50)
        processed_image = crop_to_object(bg_removed_image)
        processed_image = pad_to_square(processed_image, 100)

        # Calculate scaled dimensions

        # Determine the format based on the file extension
        file_dir, file_name = os.path.split(image_path)
        file_base, file_ext = os.path.splitext(file_name)

        # Modify the original file name to include dimensions
        new_file_name = f"{file_base}_{scaled_width}_{scaled_height}{file_ext}"
        new_file_path = os.path.join(file_dir, new_file_name)

        # Save the resized image with good quality
        os.remove(image_path)  # Remove the original file

        if file_ext == '.png':
            processed_image.save(new_file_path, format='PNG', compress_level=1)
        else:
            # Fallback to PNG if another format is requested but doesn't support transparency
            new_file_path = new_file_path.replace(file_ext, '.png')
            processed_image.save(new_file_path, format='PNG', compress_level=1)

        img.close()

        # Mark the image as processed in the database
        update_processed_image_path(new_file_path)
        print(f"Processed: {new_file_path}")

    except Exception as e:
        print(f"Error processing {image_path}: {e}")
    finally:
        # Remove the image from processing set
        processing_images.discard(image_path)



def start_folder_watcher(image_folder):
    """Start watching the image folder for changes."""
    event_handler = ImageHandler()
    observer = Observer()
    observer.schedule(event_handler, str(image_folder), recursive=True)  # Set recursive to True
    observer.start()

    # Collect all existing images for concurrent processing
    image_paths = [
        os.path.join(root, filename)
        for root, dirs, files in os.walk(image_folder)
        for filename in files if filename.lower().endswith(('.png', '.jpg', '.jpeg'))
    ]

    if image_paths:
        process_images_concurrently(image_paths)  # Process images concurrently

    return observer



def stop_folder_watcher(observer):
    """Stop the image watcher."""
    observer.stop()
    observer.join()


def remove_background(image: Image.Image) -> Image.Image:
    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    bg_removed = remove(buffered.getvalue())
    img = Image.open(io.BytesIO(bg_removed))

    # Ensure alpha channel is preserved
    if img.mode != "RGBA":
        img = img.convert("RGBA")
    return img
