#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_number = -(-number % 10) if number < 0 else number % 10
str = f"Last digit of {number} is {last_number} and is "
if (last_number > 5):
    str += "greater than 5"
elif (last_number == 0):
    str += "0"
else:
    str += "less than 6 and not 0"
print(str)
