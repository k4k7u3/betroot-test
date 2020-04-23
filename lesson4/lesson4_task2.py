import random

list_1 = []
list_2 = []
list_3 = []

i = 0
while i!= 10:
	list_1.append(random.randint(1, 10))
	list_2.append(random.randint(1, 10))
	if list_1[i] in list_2:
		if list_1[i] not in list_3:
			list_3.append(list_1[i])
	i += 1
print(list_1)
print(list_2)
print(list_3)

