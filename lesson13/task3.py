from functools import wraps


def args_rule(type_, max_length, contains):
    def decor(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for item in args:
                if type(item) != type_:
                    return False, f"Type args '{item}' should be a string"
                elif len(item) > max_length:
                    return False, f"Len -> '{item}' should be no more than {max_length}"
                if any(i not in item for i in contains):
                    return False, f"'{item}' should include {contains}"
            result = func(*args, **kwargs)
            return True, result
        return wrapper
    return decor


@args_rule(type_=str, max_length=15, contains=['a', 'y'])
def my_func(string_one, string_two):
    return string_one + ". " + string_two


str_one = "any"
str_two = "more than y"
print(my_func(str_one, str_two))
