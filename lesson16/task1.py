from _collections_abc import Iterable


def with_index(iterable, start=0):
    if not isinstance(iterable, Iterable):
        raise TypeError(f"{iterable} should be iterable")
    for item in iterable:
      yield start, item
      start += 1


x = [10, 20, 30, 40]

iterable = with_index(x, 50)
y = enumerate(x, 50)
print(next(iterable))
print(next(y))
print(next(iterable))
print(next(y))

