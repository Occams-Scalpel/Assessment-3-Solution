from class_builder import ClassBuilder


class JSClassBuilderB(ClassBuilder):

    def set_new_js_class(self):
        self.current_class = {"class_name": "",
                              "attributes": [],
                              "attribute_types": [],
                              "methods": [],
                              "class_calls": [],
                              "inherits_from": ""}

    def retrieve_class_info(self, class_ast):
        self.loop_class(class_ast)

    def loop_class(self, class_ast):

        if class_ast.type == "ClassDeclaration":
            self.current_class["class_name"] = class_ast.id.name

            if class_ast.superClass is not None:
                self.current_class["inherits_from"] = class_ast.superClass.name

            for a_method in class_ast.body.body:
                self.loop_method(a_method)

    def loop_method(self, method_ast):
        new_method = {"name": "",
                      "parameters": [], "return_type": ""}

        if method_ast.type == "MethodDefinition":
            new_method["name"] = method_ast.key.name
            for a_param in method_ast.value.params:
                new_method["parameters"].append(a_param.name)
        self.current_class["methods"].append(new_method)

        for an_expression in method_ast.value.body.body:
            self.loop_expression(an_expression, method_ast, new_method)

    def loop_expression(self, expression_ast, method_ast, new_method):
        if expression_ast.type == "ReturnStatement":
            expr_type = type(expression_ast.argument.value)
            new_method["return_type"] = f' : {expr_type.__name__}'

        e_type = expression_ast.type == "VariableDeclaration"
        if e_type and expression_ast.declarations[0].init.type == "NewExpression":
            self.current_class["class_calls"].append(
                expression_ast.declarations[0].init.callee.name)

        if expression_ast.expression is not None:
            left_value = expression_ast.expression.left
            right_value = expression_ast.expression.right

            if method_ast.key.name == "constructor":
                if left_value.object.type == "ThisExpression":
                    self.current_class["attributes"].append(
                        left_value.property.name)
                    attribute_value = right_value.value
                    if isinstance(attribute_value, type(None)):
                        value_type = ""
                    else:
                        value_type = f' : {type(attribute_value).__name__}'
                    self.current_class["attribute_types"].append(
                        value_type)

            if right_value is not None and right_value.type == "NewExpression":
                self.current_class["class_calls"].append(
                    right_value.callee.name)
