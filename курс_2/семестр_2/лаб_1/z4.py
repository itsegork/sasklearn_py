import random

number = random.randint(100, 999)

hundreds = number // 100
tens = (number % 100) // 10
units = number % 10

print(f"{hundreds}, {tens}, {units}")