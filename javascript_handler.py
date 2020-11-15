from dot_formatter import DotFormatter
from director import Director
from js_class_builder_a import JSClassBuilderA
from js_class_builder_b import JSClassBuilderB


class JavascriptHandler():
    """Responsible for converting"""

    def __init__(self, the_js: str, current_cmd: str):
        self.js_code = the_js
        self.current_cmd = current_cmd

    def extract_javascript_a(self):
        builder_a = JSClassBuilderA(self.js_code)
        director_a = Director(builder_a)
        director_a.create_class_data_set()
        self.js_code = builder_a.get_all_js_classes()

    def extract_javascript_b(self):
        builder_b = JSClassBuilderB(self.js_code)
        director_b = Director(builder_b)
        director_b.create_class_data_set()
        self.js_code = builder_b.get_all_js_classes()

    # Shared method's
    def create_puml(self):
        my_dot_formatter = DotFormatter(self.js_code)
        if self.current_cmd == "a":
            my_dot_formatter.convert_to_dot_a()
        else:
            my_dot_formatter.convert_to_dot_b()
            my_dot_formatter.handle_dot_file(self.current_cmd)
