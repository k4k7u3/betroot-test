from functools import wraps


def args_rule(type_, max_length, contains):
    def decor(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = ""
            try:
                for item in args:
                    if type(item) != type_:
                        raise ValueError
                    elif len(item) > max_length:
                        raise Exception(f"Len -> '{item}' should be no more than {max_length}")
                    for i in contains:
                        if i not in item:
                            raise Exception(f"'{item}' should include {contains}")
                result = func(*args, **kwargs)
                return True, result
            except ValueError:
                result = f"Type args '{item}' should be a string"
                return False, result
            except Exception as e:
                result = str(e)
                return False, result
        return wrapper
    return decor


@args_rule(type_=str, max_length=15, contains=['a', 'y'])
def my_func(string_one, string_two):
    return string_one + ". " + string_two

str_one = "any"
str_two = "more than 15 it is a true"
print(my_func(str_one, str_two))
