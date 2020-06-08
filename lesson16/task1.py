from _collections_abc import Iterable


def with_index(iterable, start=0):
    if not isinstance(iterable, Iterable):
        raise TypeError(f"{iterable} should be iterable")
    if start >= len(iterable):
        raise ValueError
    yield start, iterable[start]


x = [10, 20, 30, 40]

iterable = with_index(x, 1)
print(next(iterable))

