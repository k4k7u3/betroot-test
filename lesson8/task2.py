def math_fun(num):
    try:
        a = float(num[0])
        b = float(num[1])
        return((a / b) ** 2)
    except ValueError as e:
        print("It's should be only number")
    except ZeroDivisionError as e:
        print("We can't div by zero")

s = input("Input two numbers: ")
s = s.split(' ')
result = math_fun(s)
print(result)