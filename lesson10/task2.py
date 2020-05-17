class Dog:
    age_factor = 7

    def __init__(self, age):
        self.age_dog = int(age)

    def human_age(self):
        return self.age_dog * self.age_factor


my_dog = Dog(6)
print(my_dog.human_age())