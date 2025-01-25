from io import BytesIO
import sys
import os
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from PyPDF2 import PdfReader, PdfWriter

def resource_path(relative_path):
    """Returns the absolute path to a resource, handling both development and PyInstaller modes."""
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(__file__))  # Get current file directory

    # Move up to the root of the project (if needed)
    project_root = os.path.abspath(os.path.join(base_path, "../../"))  # Move two levels up
    return os.path.join(project_root, relative_path)  # Join with the relative path

def draw_image_aspect_ratio(can, ui, x=130, y=1890, target_width=220, target_height=200):
    image_lbl = getattr(ui, "label_profile")
    image_path = image_lbl.toolTip()
    if image_path == "":
        image_path = resource_path("ui/resources/default_profile.png")
        x = 130
        y = 1880

    image = ImageReader(image_path)
    original_width, original_height = image.getSize()
    aspect_ratio = original_width / original_height
    if original_width / target_width > original_height / target_height:
        # Scale based on target width
        scaled_width = target_width
        scaled_height = target_width / aspect_ratio
    else:
        # Scale based on target height
        scaled_height = target_height
        scaled_width = target_height * aspect_ratio

    can.drawImage(image_path, x, y, scaled_width, scaled_height, mask='auto')

def download_page(template_path, output_file, packet):
    with open(template_path, "rb") as template_file:
        existing_pdf = PdfReader(template_file)
        output = PdfWriter()
        new_pdf = PdfReader(packet)
        if len(existing_pdf.pages) > 0 and len(new_pdf.pages) > 0:
            template_page = existing_pdf.pages[0]
            new_page = new_pdf.pages[0]
            template_page.merge_page(new_page)
            output.add_page(template_page)

        with open(output_file, "wb") as outputStream:
            output.write(outputStream)

def wrap_text(text, max_width, font_name, font_size, can):
    """Wraps the input text to fit within the specified maximum width and returns the wrapped lines."""
    words = text.split()
    lines = []
    current_line = ""

    for word in words:
        if can.stringWidth(current_line + word, font_name, font_size) <= max_width:
            current_line += word + " "
        else:
            lines.append(current_line.strip())
            current_line = word + " "
    if current_line:
        lines.append(current_line.strip())
    return lines

def adjust_line_width(can, line, font_name, font_size, max_width):
    """Adjusts text width by reducing font size until the line fits within the specified width."""
    sentence = ""
    for word in line:
        if can.stringWidth(sentence + word, font_name, font_size) <= max_width:
            sentence += word + " "
        else:
            return False
    return True

def draw_left(text, x, y, max_width, font_name, font_size, can):
    """Draws left-aligned text, adjusting font size to fit the specified width."""
    lines = wrap_text(text, max_width, font_name, font_size, can)
    while not adjust_line_width(can, lines, font_name, font_size, max_width):
        font_size -= 0.01
        lines = wrap_text(text, max_width, font_name, font_size, can)

    can.setFont(font_name, font_size)
    for line in lines:
        can.drawString(x, y, line)

def draw_texts(can, ui):
    fonts_path = resource_path("ui/resources/fonts/static")
    font_list = ["Montserrat-Medium.ttf", "Montserrat-SemiBold.ttf", "Montserrat-Bold.ttf",
                 "Montserrat-ExtraBold.ttf",
                 "Montserrat-Black.ttf", "Montserrat-Thin.ttf", "Montserrat-Regular.ttf", "BebasNeue-Regular.ttf"]

    for item in font_list:
        font_path = resource_path(fonts_path + "/" + item)
        font = item.strip(".ttf")
        pdfmetrics.registerFont(TTFont(font, font_path))

    text_positions = [
        {'widget': "line_name", 'x': 475, 'y': 2070, 'max_width': 200, 'font_size': 16, 'align': "normal"},
        {'widget': "line_age", 'x': 765, 'y': 2070, 'max_width': 200, 'font_size': 16, 'align': "normal"}
    ]

    for label in text_positions:
        name = getattr(ui, label['widget'])
        name_text = name.text()
        if label['align'] == "normal":
            draw_left(name_text, label['x'], label['y'], label['max_width'], "Montserrat-Medium",
                      label['font_size'], can=can)


def draw_first_page(ui):
    '''
    Function to draw on the template the first page with basic information
    :param parent:
    :param ui:
    :return:
    '''
    #labels_names = WidgetsNames().get_widgets_general()
    packet = BytesIO()
    page_width = 900
    page_height = 2100
    can = canvas.Canvas(packet, pagesize=(page_width, page_height))
    can.setFillColorRGB(0,0,0)

    draw_image_aspect_ratio(can, ui, 150, 1900, 220, 200)
    draw_texts(can, ui)

    can.save()
    template_path = resource_path("ui/resources/templates/page1.pdf")  # Adjust relative path
    output_file = resource_path("output_page1.pdf")
    packet.seek(0)
    download_page(template_path, output_file, packet)


def draw_pages_and_download(ui):
    draw_first_page(ui)