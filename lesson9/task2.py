import json

menu = {
    '1': 'Add new entries',
    '2': 'Search by first name',
    '3': 'Search by last name',
    '4': 'Search by full name',
    '5': 'Search by telephone number',
    '6': 'Search by city or state',
    '7': 'Delete a record for a given telephone number',
    '8': 'Update a record for a given telephone number',
    '9': 'Exit and save'
}

json_dict = {}
info = []

pattern = {
        "name": "",
        "surname": "",
        "full name": "",
        "telephone": "",
        "city": ""
}

while True:
    json_file = open('task2.json', 'r')
    json_info = json.load(json_file)
    json_file.close()
    oper = input(f"Choose operation {menu}: ")
    oper = oper.strip().replace(" ", "")
    if oper in menu:
        if oper == '1':
            for i in pattern:
                input_info = input(f'Input {i}: ')
                json_dict[i] = input_info
            json_info.append(json_dict)
            json_file = open('task2.json', 'w+')
            json.dump(json_info, json_file, indent=4)
            json_file.close()
            continue
        if oper == '2':
            input_name = input("What name do you want to find? : ")
            for i in json_info:
                if i["name"] == input_name:
                    info.append(i)
            if len(info) != 0:
                print(info)
            else:
                print("We don't find this name")
            continue
        if oper == '3':
            input_name = input('What surname do you want to find? : ')
            for i in json_info:
                if i["surname"] == input_name:
                    info.append(i)
            if len(info) != 0:
                print(info)
            else:
                print("We don't find this surname")
            continue
        if oper == '4':
            input_name = input('What full name do you want to find? : ')
            for i in json_info:
                if i["full name"] == input_name:
                    info.append(i)
            if len(info) != 0:
                print(info)
            else:
                print("We don't find this full name")
            continue
        if oper == '5':
            input_name = input('What telephone number do you want to find? : ')
            for i in json_info:
                if i["telephone"] == input_name:
                    info.append(i)
            if len(info) != 0:
                print(info)
            else:
                print("We don't find this number")
            continue
        if oper == '6':
            input_name = input('What city do you want to find? : ')
            for i in json_info:
                if i["city"] == input_name:
                    info.append(i)
            if len(info) != 0:
                print(info)
            else:
                print("We don't find this city")
            continue
        if oper == '7':
            number = input("Input number to delete a record by number : ")
            for i in json_info:
                if i["telephone"] == number:
                    json_info.remove(i)
            json_file = open('task2.json', 'w+')
            json.dump(json_info, json_file, indent=4)
            json_file.close()
            continue
        if oper == '8':
            number = input("Input number to delete a record by number : ")
            for i in json_info:
                if i["telephone"] == number:
                    for j in i:
                        input_info = input(f'Input {j}: ')
                        i[j] = input_info
            json_file = open('task2.json', 'w+')
            json.dump(json_info, json_file, indent=4)
            json_file.close()
            continue
        if oper == '9':
            print("Thank You! Good Bye =) ")
            break
    else:
        print('Dead')
    break
