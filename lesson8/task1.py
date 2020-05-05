def oops():
    raise IndexError("It's my Index Error")


def oh_my_god():
    try:
        oops()
    except ValueError as e:
        print(e)
    except Exception as e:
        print("We don't have IndexError exception")

oh_my_god()