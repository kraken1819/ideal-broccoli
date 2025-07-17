# Class method decorator
def custom_method_decorator(func):

    def wrapper(cls, *args, **kwargs):
        print("before the class method call")
        func(cls, *args, **kwargs)
        print("after the class method call")

    return wrapper

class A: 
    @custom_method_decorator
    def print_values(a,b):
            print(a, b)


a_obj = A()
A.print_values(5,20);
