from typing import NoReturn

class Myclass:
    def __init__(self, inputStr: str) -> NoReturn:
        self.classStr: str = inputStr
        self.squareBrackets: int = 0
        self.parentheses: int = 0
        self.curlyBrackets: int = 0

    def balanced(self) -> NoReturn:
        for i in self.classStr:
            if i == "(":
                self.curlyBrackets += 1
            elif i == ")":
                self.curlyBrackets -= 1
            elif i == "[":
                self.squareBrackets += 1
            elif i == "]":
                self.squareBrackets -= 1
            elif i == "{":
                self.parentheses += 1
            elif i == "}":
                self.parentheses -= 1
        if self.curlyBrackets == 0 and self.squareBrackets == 0 and self.parentheses == 0:
            print("Perfect balance (c) Thanos")
        else:
            print("Not enough stones")


balanced = "(){{}[]]"
mystr = Myclass(balanced)
mystr.balanced()
