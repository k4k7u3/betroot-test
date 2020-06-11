def count_lines(name):
    if type(name) != str:
        raise ValueError(f"'{name}' should be a string")
    with open(f"{name}", "r") as open_file:
        len_str = len(open_file.readlines())
        return len_str


def count_chars(name):
    if type(name) != str:
        raise ValueError(f"'{name}' should be a string")
    with open(f"{name}", "r") as open_file:
        count_char = open_file.read()
        return len(count_char)


def test(name):
    if type(name) != str:
        raise ValueError(f"'{name}' should be a string")
    cnt_lines = count_lines(name)
    cnt_chars = count_chars(name)
    return f"Lines: {cnt_lines}, Chars: {cnt_chars}"
