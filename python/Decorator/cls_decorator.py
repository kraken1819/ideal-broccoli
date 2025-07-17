# Class Decorator 

def custom_class_decorator(cls):
    cls.__name__ = "custom_class_by_kraken"

    return cls

@custom_class_decorator
class A:
    pass

print(A.__name__)
