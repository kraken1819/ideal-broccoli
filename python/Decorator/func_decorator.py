# Function Decorator
def custom_decorator(func):

    def wrapper(a, b):
        print("before the function call")
        func(a, b)
        print("after the function call")

    return wrapper

@custom_decorator
def perform_max(a, b):
    print(max(a,b))

perform_max(5,10)
