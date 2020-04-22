import random
import math

s = input('Input something: ')
x = 0
st = list(s)
while x != 5:
	random.shuffle(st)
	print(st)
	x += 1
