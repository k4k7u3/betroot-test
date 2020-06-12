def in_range(start, end=0, step=1):
    if type(start) != int and type(end) != int and type(step) != int:
        raise ValueError
    if step == 0:
        raise ValueError("'Step' should not be a zero")
    elif step > 0:
        if start > end:
            while end <= start-1:
                yield end
                end += 1
        else:
            while start <= end-1:
                yield start
                start += step
    else:
        while start >= end+1:
            yield start
            start += step


x = in_range(10, 5, -1)
for i in x:
    print(i)




