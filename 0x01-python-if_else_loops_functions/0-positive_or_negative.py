#!/usr/bin/python3
import random
number = random.randint(-10, 10)
print(f'{number:d} ', end="")
if number > 0:
    print('is positive')
elif number == 0:
    print('is zero')
elif number < 0:
    print('is negative')
else:
    print('TypeError')