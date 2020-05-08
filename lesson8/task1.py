def oops():
    raise IndexError("It's my Index Error")


def oh_my_god():
    try:
        oops()
    except ValueError as e:
        print(e)
    except IndexError as e:
        print(e)

oh_my_god()
