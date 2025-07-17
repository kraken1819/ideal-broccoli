# chained decorator

def cus_decor_1(func):

    def wrapper(*args,**kwargs):
        # modifies args 
        args_list = list(args)
       
        for i in range(len(args_list)):
            args_list[i] = 2*args_list[i]
        args = tuple(args_list)
        
        return func(*args, **kwargs)

    return wrapper

def cus_decor_2(func):

    def wrapper(*args,**kwargs):
        # modifies args
        args_list = list(args)
        for i in range(len(args_list)):
            args_list[i] = args_list[i] - 1
        args = tuple(args_list)

        return func(*args, **kwargs)
    
    return wrapper

@cus_decor_2
@cus_decor_1
def func1(a):
    return a

@cus_decor_1
@cus_decor_2
def func2(a):
    return a


print(func1(5))
print(func2(5))
