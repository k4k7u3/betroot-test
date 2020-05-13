# import json
#
# new_file = open('new_file', 'r')
# json_info = json.load(new_file)
# print(json_info)
# new_file.close()

s = [
    {
        "name": "sasha",
        "surname": "but",
        "full_name": "sahsa but",
        "telephone": "0994897214",
        "city": "kharkov"
    },
    {
        "name": "alina",
        "surname": "but",
        "full_name": "sahsa but",
        "telephone": "0994897214",
        "city": "kharkov"
    },
    {
        "name": "mary",
        "surname": "but",
        "full_name": "sahsa but",
        "telephone": "0994897214",
        "city": "kharkov"
    }
]
for i in s:
    if i["name"] == "mary":
        s.remove(i)
print(s)