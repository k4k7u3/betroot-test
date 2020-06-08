class My_iter:
    def __init__(self, *args):
        self.args = args
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.args):
            raise StopIteration
        value = self.args[self.index]
        self.index += 1
        return value


x = My_iter(1, 2, 3, 4, 5)

for i in x:
    print(i)