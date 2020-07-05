from typing import Any, NoReturn, List

class MyStack:
    def __init__(self) -> NoReturn:
        self.stacklist = []

    def push(self, item: List[Any]) -> NoReturn:
        self.stacklist = [i for i in item]

    def pop(self) -> Any:
        return self.stacklist.pop()

    def print_stack(self) -> NoReturn:
        self.stacklist = [self.pop() for item in range(len(self.stacklist))]
        print(self.stacklist)

my_list = [1, 2, 3, 4, 5, 6, 7, 8]
stack = MyStack()
stack.push(my_list)
stack.print_stack()

