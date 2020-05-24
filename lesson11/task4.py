class CustomException(Exception):
    def __init__(self, msg):
        open_file = open('logs.txt', 'a+')
        open_file.write(str(msg) + str('\n'))
        open_file.close()

    def __str__(self):
        return 'My custom Exception'

    def __repr__(self):
        return 'My custom Exception'

try:
    raise CustomException('My first custom Exception')
except CustomException as e:
    print(e)
