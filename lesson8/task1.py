def oops():
    raise IndexError("It's my Index Error")


def oh_my_god():
    try:
        oops()
    except IndexError as e:
        print(e)

oh_my_god()
#  What happens if you change oops to raise KeyError instead of IndexError?
# Если у нас не будет except "ошибка которую мы ожидаем" а будет другая ошибка и нет общего Exception , то программа закроется с ошибкой 
