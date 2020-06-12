def in_range(start, end=0, step=1):
    if type(start) != int and type(end) != int and type(step) != int:
        raise ValueError
    if step == 0:
        raise ValueError("'Step' should not be a zero")
    if step >= 1:
        if end == 0:
            while end <= start-1:
                yield end
                end += step
        if end < 0 or end > 0:
            if start < end:
                while start <= end-1:
                    yield start
                    start += step
            if start > end:
                return []
    if step < 0:
        if end > start:
            return []
        if start > end:
            while start >= end+1:
                yield start
                start += step

x = in_range(10, 12)
y = range(10, 12)
print("x")
for i in x:
    print(i)
print("y")
for i in y:
    print(i)



