class Person:
    name = None
    surname = None
    age = None

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def talk(self):
        print(f"Hello, my name is {self.name} {self.surname} and i'm {self.age} years old")


my_name = Person("Sasha", "Butenko", 25)
my_name.talk()