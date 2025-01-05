
class WidgetsNames:
    def __init__(self):
        self.setup_ui()

    def setup_ui(self):
        self.widgets_general = ["username", "line_planID", "label_profile", "line_name",
                                "line_weight", "line_mg", "line_objectives", "line_date", "line_appoint", "line_meals"]
        self.widgets_page_simple = ["plain_new", "plain_new2"]
        self.widgets_page_complex = [] # to be added
        self.widgets_page_mid = [] # to be added

    def get_widgets_general(self):
        return self.widgets_general

    def get_widgets_page_simple(self):
        return self.widgets_page_simple