import random

x = []
i = 10
while i != 0:
	x.append(random.randint(0, 100))
	i -= 1
print('Вот список из случайных чисел: ', x)
big = x[0]
while i != 10:
	if big > x[i]:
		pass
	else:
		big = x[i]
	i += 1
print('Наибольшее число из списка - ', big)