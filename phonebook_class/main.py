import json

menu = {
    '1': 'Add new entries',
    '2': 'Global search',
    '3': 'Delete a record for a given telephone number',
    '4': 'Update a record for a given telephone number',
    '9': 'Exit and save'
}


json_dict = {}
info = []
list_class = []
search_info = {}
pattern = ["name", "surname", "full name", "telephone", "city"]
global_search = ["name", "surname", "full name", "telephone", "city"]


class Person:
    name = ""
    surname = ""
    full_name = ""
    telephone = ""
    city = ""

    def __init__(self, name, surname, full_name, telephone, city):
        self.name = name
        self.surname = surname
        self.full_name = self.name + ' ' + self.surname
        self.telephone = telephone
        self.city = city

    def __str__(self):
        return f'{self.name} from {self.city}'

    def __repr__(self):
        return f'{self.name} from {self.city}'

    def get_info(self):
        self.surname = input("Input surname: ")
        self.full_name = self.name + ' ' + self.surname
        self.telephone = input("Input telephone: ")
        self.city = input("Input city: ")

    def get_dict(self):
        return {
            "name": self.name,
            "surname": self.surname,
            "full_name": self.name + ' ' + self.surname,
            "telephone": self.telephone,
            "city": self.city
            }

    def search(self, mod, input_value):
        for attr, value in self.__dict__.items():
            if attr == mod and value == input_value:
                return True
        return False


def pre_initialization():
    if len(json_info) > 0:
        for i in json_info:
            list_class.append(Person(**i))


def search_info(mod):
    input_info = input(f"What {mod} do you want to find? : ")
    info = []
    for i in list_class:
        ret = i.search(mod, input_info)
        if ret is True:
            info.append(i)
    if len(info) != 0:
        print(info)
    else:
        print("We don't find anything. Try again")


try:
    try:
        json_file = open('phone.json', 'r')
        json_info = json.load(json_file)
    except json.decoder.JSONDecodeError:
        json_info = []
    json_file.close()
    pre_initialization()
    while True:
        oper = input(f"Choose operation {menu}: ")
        oper = oper.strip().lower()
        if oper in menu:
            if oper == '1':
                input_name = input("Input name: ")
                input_surname = input("Input surname: ")
                input_tel = input("Input telephone: ")
                input_city = input("Input city: ")
                created_person = Person(input_name, input_surname, input_tel, input_city)
                list_class.append(created_person)
                continue
            elif oper == '2':
                search_method = input("Input search method( name, surname, full name, telephone, city) : ")
                if search_method not in global_search:
                    print("Incorrect input")
                    continue
                else:
                    search_info(search_method)
                    continue
            elif oper == '3':
                number = input("Input number to delete a record by number : ")
                for i in list_class:
                    if i.telephone == number:
                        temporary_info = i.get_dict()
                        print(temporary_info)
                        while True:
                            y_n = input("Are you really wanna delete this record? (1 - yes, 2 - no)? ")
                            if y_n == "1":
                                list_class.remove(i)
                                break
                            elif y_n == "2":
                                break
                            else:
                                print("Incorrect input")
                continue
            elif oper == '4':
                number = input("Input number to update a record by number : ")
                for i in list_class:
                    if i.telephone == number:
                        i.name = input("Input name: ")
                        i.get_info()
                continue
            if oper == '9':
                print("Thank You! Good Bye =) ")
                break
        else:
            print("Incorrect input")
except Exception as e:
    print(e)
    print("Error")
finally:
    for i in list_class:
        json_dict = i.get_dict()
        info.append(json_dict)
    with open('phone.json', 'w+') as json_file:
         json.dump(info, json_file, indent=4)
print("Good Bye")