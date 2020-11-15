from class_builder import ClassBuilder


class JSClassBuilderA(ClassBuilder):
    def __init__(self, new_js_code):
        super().__init__(new_js_code)
        self.overall_class_attributes = []
        self.count = 0
        self.current_class_methods = []
        self.current_class_method_return_values = []
        self.current_class_method_params = {}
        self.current_class_attributes = []
        self.current_class_attribute_values = []
        self.current_class_associations = []
        self.method_count = 0
        self.current_method_value = ""

    def set_new_js_class(self):
        self.current_class = {
            "class_name": "",
            "class_attributes": [],
            "class_attribute_values": [],
            "class_methods": [],
            "class_method_values": [],
            "class_method_params": {},
            "class_associations": [],
            "class_parent": ""
        }

        self.current_class_methods = []
        self.current_class_method_return_values = []
        self.current_class_method_params = {}
        self.current_class_attributes = []
        self.current_class_attribute_values = []
        self.current_class_associations = []
        self.method_count = 0

    def retrieve_class_info(self, class_ast):
        self.loop_class(class_ast)

    def loop_class(self, class_ast):
        self.current_class["class_name"] = class_ast.id.name
        my_methods = self.ast_tree[self.count].body.body

        if class_ast.superClass is not None:
            self.current_class["class_parent"] = class_ast.superClass.name

        self.count += 1

        for a_method in my_methods:
            self.loop_method(a_method)

    def loop_method(self, method):
        self.current_method_value = ""

        for e in method.value.body.body:
            if method.key.name == "constructor":
                if e.expression.left.object.type == "ThisExpression":
                    current_attribute = e.expression.left.property.name
                    current_attribute_value = e.expression.right.value
                    self.current_class_attributes.append(current_attribute)
                    self.current_class_attribute_values.append(
                        current_attribute_value)

            is_var = e.type == "VariableDeclaration"
            if is_var and e.declarations[0].init.type == "NewExpression":
                self.current_class["class_associations"].append(
                    e.declarations[0].init.callee.name)

            if e.expression is not None:
                if e.expression.right is not None:
                    if e.expression.right.type == "NewExpression":
                        self.current_class["class_associations"].append(
                            e.expression.right.callee.name)

        self.current_class["class_attributes"] = self.current_class_attributes
        self.current_class["class_attribute_values"] = self.current_class_attribute_values
        self.current_class["class_associations"] = self.current_class_associations
        self.overall_class_attributes.append(self.current_class_attributes)

        self.current_class_methods.append(method.key.name)
        current_params = method.value.params
        self.current_class_method_params[f'{method.key.name}'] = []

        for p in current_params:
            self.current_class_method_params[f'{method.key.name}'].append(p.name)

        self.method_count += 1

        for expression_ast in method.value.body.body:
            self.loop_expression(expression_ast)

    def loop_expression(self, e):
        if e.type == "ReturnStatement":
            self.current_method_value = type(e.argument.value).__name__

        if self.current_method_value == "":
            self.current_method_value = "void"

        self.current_class_method_return_values.append(self.current_method_value)
        self.current_class["class_methods"] = self.current_class_methods
        self.current_class["class_method_values"] = self.current_class_method_return_values
        self.current_class["class_method_params"] = self.current_class_method_params
