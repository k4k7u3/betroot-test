import time
from functools import wraps


def replace_stop_word(my_list):
    def loger(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            my_str = func()
            print(my_str)
            for item in my_list:
                if item in my_str:
                my_str = my_str.replace(item, "*")
            return my_str
        return wrapper
    return loger


x = ["pepsi", "Audi"]


@replace_stop_word(x)
def my_text():
  return "I wanna drink cold pepsi in my Audi"

print(my_text())