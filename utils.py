import functools
import time
"""
usage:
def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args,**kwargs):
        return func(*args,**kwargs)
    return wrapper_decorator
"""


def timer(func):
    @functools.wraps(func)
    def wrapper_decorator(*args,**kwargs):
        start = time.perf_counter()
        value = func(*args,**kwargs)
        end = time.perf_counter()
        run_time = end-start
        print(f"{run_time} secs passed...")
        return value
    return wrapper_decorator

def silly_intro(func):
    @functools.wraps(func)
    def wrapper_decorator(*args,**kwargs):
        print("Hey! Thank you so much for choosing to support us in "
            "yet another way. It really means the world to us. "
            "Every contribution you make, big or small helps us "
            "along our journey to becoming the best app. ")
        value = func(*args,**kwargs)
        return value
    return wrapper_decorator

def pretend_busy(func):
    @functools.wraps(func)
    def wrapper_decorator(*args,**kwargs):
        time.sleep(1)
        value = func(*args,**kwargs)
        return value
    return wrapper_decorator
    
def callin(func):
    @functools.wraps(func)
    def wrapper_decorator(*args,**kwargs):
        print("Brrr..Brrr..........brrr..brrr...........brrr..brrrr...........")
        value = func(*args,**kwargs)
        return value
    return wrapper_decorator
        
