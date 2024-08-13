# #write a decorator that measures time a function takes to execute

# import time

# def timer(func):
#     def wrapper(*args, **kwargs):
#         start=time.time()
#         result= func(*args, **kwargs)
#         end= time.time()
#         print(f"{func.__name__} ran in {end-start} seconds")
#         return result
#     return wrapper

# @timer
# def example(n):
#     print(n*n)
# example(5)

# # Create a decorator to print the function name and the values of its arguments every time the function is called

# def debug(func):
#     def wrapper(*args, **kwargs):
#         args_value = ', '.join(str(arg) for arg in args)
#         kwargs_value = ', '.join(f"{k}={v}" for k, v in kwargs.
#         items())
#         print(f"calling: {func.__name__} with args: {args_value} and kwargs: {kwargs_value}")
#         return func(*args, **kwargs)
    
#     return wrapper

# @debug
# def hello():
#     print("hello")

# @debug
# def greet(name, greeting="Hello"):
#     print(f"{greeting}, {name}")

# hello()
# greet("frence", greeting="bonjour")

## implement a decorator that caches the return values of a function, so that when it's called with the same arguments, the cached value is returned instead of re-executing the function
import time
def cache(func):
    cache_value= {}
    print(cache_value)
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result=func(*args)
        cache_value[args]=result
        return result
    return wrapper

@cache
def time_function(a,b):
    time.sleep(4)
    return a+b

print(time_function(1,3))
print(time_function(8,9))