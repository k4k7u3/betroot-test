from typing import NoReturn

class Myclass:
    def __init__(self, inputStr: str) -> NoReturn:
        self.classStr: str = inputStr
        self.stack = []
        self.opposite = ""

    def balanced(self):
        if len(self.classStr) % 2 != 0:
            return "Not Balanced"
        else:
            self.stack.append(self.classStr[0])
            self.classStr = self.classStr[1:]
            self.search_balanced()
            print(self.opposite)

    def search_balanced(self) -> str:
        self.check_opposite(self.classStr[0])
        if len(self.classStr) == 0 and len(self.stack) == 0:
            self.opposite = "Perfect Balanced (c) THANOS"
            return
        elif len(self.classStr) == 0 and len(self.stack) != 0:
            self.opposite = "Not Balanced"
            return
        self.search_balanced()

    def check_opposite(self, a: str):
        if self.stack == [] and len(self.classStr) != 0:
            self.stack.append(a)
            self.classStr = self.classStr[1:]
        elif self.stack[-1] == "(" and a == ")":
            self.stack.pop()
            self.classStr = self.classStr[1:]
        elif self.stack[-1] == "[" and a == "]":
            self.stack.pop()
            self.classStr = self.classStr[1:]
        elif self.stack[-1] == "{" and a == "}":
            self.stack.pop()
            self.classStr = self.classStr[1:]
        else:
            self.stack.append(a)
            self.classStr = self.classStr[1:]

balanced = "()({[][]})"
mystr = Myclass(balanced)
mystr.balanced()


