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
pattern = ["name", "surname", "full name", "telephone", "city"]
global_search = ["name", "surname", "full name", "telephone", "city"]


def search_info(mod):
    input_name = input(f"What {mod} do you want to find? : ")
    info = []
    for i in json_info:
        if i[mod] == input_name:
            info.append(i)
    if len(info) != 0:
        print(info)
    else:
        print(f"We don't find this {mod}")
    return None


def json_record():
    json_file = open('task2.json', 'w+')
    json.dump(json_info, json_file, indent=4)
    json_file.close()


try:
    try:
        json_file = open('task2.json', 'r')
        json_info = json.load(json_file)
    except json.decoder.JSONDecodeError:
        json_info = []
    json_file.close()
    while True:
        oper = input(f"Choose operation {menu}: ")
        oper = oper.strip().lower()
        if oper in menu:
            if oper == '1':
                for i in pattern:
                    input_info = input(f'Input {i}: ')
                    input_info = input_info.strip().lower()
                    json_dict[i] = input_info
                json_info.append(json_dict)
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
                for i in json_info:
                    if i["telephone"] == number:
                        print(i)
                        while True:
                            y_n = input("Are you really wanna delete this record? (1 - yes, 2 - no)? ")
                            if y_n == "1":
                                json_info.remove(i)
                                break
                            elif y_n == "2":
                                break
                            else:
                                print("Incorrect input")
                continue
            elif oper == '4':
                number = input("Input number to update a record by number : ")
                for i in json_info:
                    if i["telephone"] == number:
                        for j in i:
                            input_info = input(f'Input {j}: ')
                            input_info = input_info.strip().lower()
                            i[j] = input_info
                continue
            if oper == '9':
                json_record()
                print("Thank You! Good Bye =) ")
                break
        else:
            print("Incorrect input")
except Exception:
    print("Error")
finally:
    with open('task2.json', 'w+') as json_file:
        json.dump(json_info, json_file, indent=4)
print("Good Bye")