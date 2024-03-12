#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

the_last_digit = number % 10 if number > 0 else abs(number) % 10 * -1

print(f"Last digit of {number} is {the_last_digit}", end='')

if the_last_digit > 5:
    print(" and is greater than 5")
elif the_last_digit == 0:
    print(" and is 0")
else:
    print(" and is less than 6 and not 0")
