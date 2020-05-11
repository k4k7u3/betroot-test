import json

menu = {
    '1': 'Add new entries',
    '2': 'Global search',
    '3': 'Delete a record for a given telephone number',
    '4': 'Update a record for a given telephone number',
    '9': 'Exit and save'
}

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


json_dict = {}
info = []

pattern = {
        "name": "",
        "surname": "",
        "full name": "",
        "telephone": "",
        "city": ""
}
try:
    while True:
        try:
            json_file = open('task2.json', 'r')
            json_info = json.load(json_file)
        except json.decoder.JSONDecodeError:
            json_info = []
        json_file.close()
        oper = input(f"Choose operation {menu}: ")
        oper = oper.strip().lower()
        if oper in menu:
            if oper == '1':
                for i in pattern:
                    input_info = input(f'Input {i}: ')
                    input_info = input_info.strip().lower()
                    json_dict[i] = input_info
                json_info.append(json_dict)
                json_file = open('task2.json', 'w+')
                json.dump(json_info, json_file, indent=4)
                json_file.close()
                continue
            if oper == '2':
                search_method = input("Input search method( name, surname, full name, telephone, city) : ")
                if search_method not in global_search:
                    print("Incorrect input")
                    continue
                else:
                    search_info(search_method)
                    continue
            if oper == '3':
                number = input("Input number to delete a record by number : ")
                for i in json_info:
                    if i["telephone"] == number:
                        json_info.remove(i)
                json_file = open('task2.json', 'w+')
                json.dump(json_info, json_file, indent=4)
                json_file.close()
                continue
            if oper == '4':
                number = input("Input number to update a record by number : ")
                for i in json_info:
                    if i["telephone"] == number:
                        for j in i:
                            input_info = input(f'Input {j}: ')
                            input_info = input_info.strip().lower()
                            i[j] = input_info
                json_file = open('task2.json', 'w+')
                json.dump(json_info, json_file, indent=4)
                json_file.close()
                continue
            if oper == '9':
                print("Thank You! Good Bye =) ")
                break
        else:
            print('Incorrect input')
            continue
        break
except Exception:
    print("Error")
finally:
    with open('task2.json', 'w+') as json_file:
        json.dump(json_info, json_file, indent = 4)
print("Good Bye")