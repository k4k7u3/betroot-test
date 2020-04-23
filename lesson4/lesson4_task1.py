import random

x = []
i = 0
big = 0
while i != 10:
	x.append(random.randint(0, 100))
	if x[i] > big:
		big = x[i]
	i += 1

print('Вот список из случайных чисел: ', x)
print('Наибольшее число из списка - ', big)
