#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
#print(f'{number:d} ', end="")
if number > 0:
    print(f'{number:.2d} is positive')
elif number == 0:
    print(f'{number:.2d} is zero')
elif number < 0:
    print(f'{number:.2d} is negative')
else:
    print('TypeError')
