
from class_builder import ClassBuilder


class Director:

    def __init__(self, new_builder: ClassBuilder):
        self.my_builder = new_builder

    def create_class_data_set(self):
        self.my_builder.parse_javascript()

        for a_class in self.my_builder.ast_tree:
            self.my_builder.set_new_js_class()
            self.my_builder.retrieve_class_info(a_class)
            self.my_builder.add_class_to_dataset()
