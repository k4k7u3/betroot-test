def import_fun(value):
    if type(value) != int and type(value) != float:
        raise ValueError(f"'{value}' must be a number")
    return value*value
