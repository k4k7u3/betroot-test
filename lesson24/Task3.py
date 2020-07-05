from typing import Any, NoReturn, List

class MyStack:
    def __init__(self) -> NoReturn:
        self.stacklist = []
        self.item = None

    def push(self, item: List[Any]) -> NoReturn:
        self.stacklist = [i for i in item]

    def pop(self) -> Any:
        return self.stacklist.pop()

    def print_stack(self) -> NoReturn:
        self.stacklist = [self.pop() for item in range(len(self.stacklist))]
        print(self.stacklist)

    def get_from_stack(self, item: Any) -> Any:
        for i in range(len(self.stacklist)):
            a = self.pop()
            if a == item:
                self.item = a
            else:
                self.stacklist.insert(0, a)
        if self.item == None:
            raise ValueError("We didn't find your item in our stack")
        print(self.stacklist)
        return self.item


my_list = [1, 2, 3, 4, 5, 6, 7, 8]
stack = MyStack()
stack.push(my_list)
# stack.print_stack()
print(stack.get_from_stack(2))

