#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    number *= -1
    lastnum = (number % 10) * -1
    number *= -1
else:
    lastnum = number % 10
if lastnum > 5:
    laststr = 'and is greater than 5'
elif lastnum == 0:
    laststr = 'and is 0'
else:
    laststr = 'and is less than 6 and not 0'
print(f'Last digit of {number} is {lastnum} {laststr}')
