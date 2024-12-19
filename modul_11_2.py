import inspect

def introspection_info(obj):
    obj_type = type(obj).__name__
    obj_dir = dir(obj)
    attributes = [attr for attr in obj_dir if not callable(getattr(obj, attr))]
    methods = [method for method in obj_dir if callable(getattr(obj, method))]
    obj_module = getattr(obj, "__module__", "Built-in or None")
    docstring = inspect.getdoc(obj) or "No docstring available"
    is_class = inspect.isclass(obj)
    is_function = inspect.isfunction(obj)
    is_module = inspect.ismodule(obj)
    return {
        "type": obj_type,
        "attributes": attributes,
        "methods": methods,
        "module": obj_module,
        "docstring": docstring,
        "is_class": is_class,
        "is_function": is_function,
        "is_module": is_module,
    }
class MyClass:
    def __init__(self, value):
        self.value = value
    def greet(self):
        return f"Hello, my value is {self.value}!"
my_object = MyClass(10)
info = introspection_info(my_object)
print(info)
number_info = introspection_info(42)
print(number_info)
