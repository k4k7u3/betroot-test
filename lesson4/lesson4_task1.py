import random

x = []
i = 0
while i != 10:
	x.append(random.randint(0, 100))
	i += 1
print('Вот список из случайных чисел: ', x)
print('Наибольшее число из списка - ', max(x))
