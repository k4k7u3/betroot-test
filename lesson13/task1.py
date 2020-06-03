from functools import wraps


def loger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} called with {args}")
    return wrapper


@loger
def add(x, y):
    return x + y

add(4, 5)