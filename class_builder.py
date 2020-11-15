from abc import ABC, abstractmethod
from esprima import parseScript


class ClassBuilder(ABC):
    def __init__(self, new_js_code):
        self.js_code = new_js_code
        self.current_class = None
        self.ast_tree = None
        self.all_js_classes = []

    def get_all_js_classes(self):
        return self.all_js_classes

    def parse_javascript(self):
        self.ast_tree = parseScript(self.js_code).body

    def add_class_to_dataset(self):
        self.all_js_classes.append(self.current_class)

    @abstractmethod
    def set_new_js_class(self):
        pass

    @abstractmethod
    def retrieve_class_info(self, new_class_ast):
        pass
