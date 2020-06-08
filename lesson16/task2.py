def in_range(start, end, step = 1):
    if type(start) != int and type(end) != int:
        raise ValueError
    while start <= end-1:
        yield start
        start += step


x = in_range(0, 20, 1)
for i in x:
    print(i)




