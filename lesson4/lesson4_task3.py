import random

x = []
z = []
i = 0
while i != 100:
	x.append(i+1)
	if x[i] % 7 == 0 and x[i] % 5 != 0:
		z.append(x[i])
	i += 1
print(x)
print(z)
