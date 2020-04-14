name = "sasha"

input_name = input("Введите свое имя: ")

if name == input_name or (input_name.istitle() == True and name[0] == input_name[0].lower()): 
	print("Имя совпадает")
else:
	print("Имя не совпадает")
