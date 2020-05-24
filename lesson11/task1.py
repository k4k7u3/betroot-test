class Person:
    name = ''
    surname = ''
    male = ''


class Student(Person):
    marks_per_semesters = {}
    final_marks = {}
    lessons = None
    number_of_class = None

    def get_final_mark(self):
        return self.final_marks
    pass


class Teacher(Person):
    wages = None
    experience = None
    dress_code = None
    taxes = None
    category = None

    def calculate_wages(self):
        return self.wages + (self.experience * 250) + (self.category * 200) - self.taxes  # for example
    pass

