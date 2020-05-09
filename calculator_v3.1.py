import random
import math

s = input(': ')

if s[0] == '-' and s.count('-') == 1:
	s = s.replace('-', '')
	print(s)
else:
	print('Flase')
