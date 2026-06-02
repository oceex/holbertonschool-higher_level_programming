#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    lst = number%10
else:
    lst = number%-10
if lst == 0:
    print(f"Last digit of {number} is 0 and is 0")
elif lst > 5:
    print(f"Last digit of {number} is {lst} and is greater than 5")
else:
    print(f"Last digit of {number} is {lst} and is less than 6 and not 0")
