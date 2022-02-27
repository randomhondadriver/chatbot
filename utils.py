import functools

"""
usage:
def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args,**kwargs):
        return func(*args,**kwargs)
    return wrapper_decorator
"""
