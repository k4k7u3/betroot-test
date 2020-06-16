import json
from typing import Union, Tuple, List, Dict, Iterable, Iterator, Any, Optional

menu: Dict[str, str] = {
    '1': 'Add new entries',
    '2': 'Global search',
    '3': 'Delete a record for a given telephone number',
    '4': 'Update a record for a given telephone number',
    '9': 'Exit and save'
}


json_dict: Dict = {}
info: List[...] = []
list_class: List[str] = []
search_info: Dict = {}
pattern: List[str] = ["name", "surname", "full name", "telephone", "city"]
global_search: List[str] = ["name", "surname", "full name", "telephone", "city"]


class Person:
    name: str = ""
    surname: str = ""
    full_name: str = ""
    telephone: str = ""
    city: str = ""

    def __init__(self, name: str, surname: str, telephone: str, city: str) -> None:
        self.name: str = name
        self.surname: str = surname
        self.full_name: str = self.name + ' ' + self.surname
        self.telephone: str = telephone
        self.city: str = city

    def __str__(self) -> str:
        return f'{self.name} from {self.city}'

    def __repr__(self) -> str:
        return f'{self.name} from {self.city}'

    def get_info(self) -> None:
        self.surname: str = input("Input surname: ")
        self.full_name: str = self.name + ' ' + self.surname
        self.telephone: str = input("Input telephone: ")
        self.city: str = input("Input city: ")
        return None

    def get_dict(self) -> Dict[str, str]:
        return {
            "name": self.name,
            "surname": self.surname,
            "full_name": self.name + ' ' + self.surname,
            "telephone": self.telephone,
            "city": self.city
            }

    def search(self, mod: str, input_value: str) -> bool:
        for attr, value in self.__dict__.items():
            if attr == mod and value == input_value:
                return True
        return False


def pre_initialization() -> None:
    if len(json_info) > 0:
        for i in json_info:
            list_class.append(Person(**i))
    return None


def search_info(mod: str) -> None:
    input_info: str = input(f"What {mod} do you want to find? : ")
    info: List[str] = []
    for i in list_class:
        ret = i.search(mod, input_info)
        if ret is True:
            info.append(i)
    if len(info) != 0:
        print(info)
    else:
        print("We don't find anything. Try again")
    return None


try:
    try:
        json_file = open('phone.json', 'r')
        json_info: List[...] = json.load(json_file)
    except json.decoder.JSONDecodeError:
        json_info = []
    json_file.close()
    pre_initialization()
    while True:
        oper: str = input(f"Choose operation {menu}: ")
        oper = oper.strip().lower()
        if oper in menu:
            if oper == '1':
                input_name: str = input("Input name: ")
                input_surname: str = input("Input surname: ")
                input_tel: str = input("Input telephone: ")
                input_city: str = input("Input city: ")
                created_person = Person(input_name, input_surname, input_tel, input_city)
                list_class.append(created_person)
                continue
            elif oper == '2':
                search_method: str = input("Input search method( name, surname, full name, telephone, city) : ")
                if search_method not in global_search:
                    print("Incorrect input")
                    continue
                else:
                    search_info(search_method)
                    continue
            elif oper == '3':
                number: str = input("Input number to delete a record by number : ")
                for i in list_class:
                    if i.telephone == number:
                        temporary_info: Dict[str, str] = i.get_dict()
                        print(temporary_info)
                        while True:
                            y_n: str = input("Are you really wanna delete this record? (1 - yes, 2 - no)? ")
                            if y_n == "1":
                                list_class.remove(i)
                                break
                            elif y_n == "2":
                                break
                            else:
                                print("Incorrect input")
                continue
            elif oper == '4':
                number: str = input("Input number to update a record by number : ")
                for i in list_class:
                    if i.telephone == number:
                        i.name: str = input("Input name: ")
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
        json_dict: Dict[str, str] = i.get_dict()
        info.append(json_dict)
    with open('phone.json', 'w+') as json_file:
         json.dump(info, json_file, indent=4)
print("Good Bye")