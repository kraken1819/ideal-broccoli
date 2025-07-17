## Decorators in python

### Definition 

Decoratos in python is a flexible way to extend (or) modify the behaviour of a method (or) function without actually changing the function


### Entities on which decorator can be used

1. Function 
2. Method
3. Class

### Samples code

```
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
```

Output
```
before the function call
10
after the function call
```
### Explanation

* The Decorator function takes the main function as an argument 
* returns modifies/extends the actual function

