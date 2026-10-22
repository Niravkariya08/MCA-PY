#Write a program to generate random numbers using random module.

import random 

value1 = int(input("Enter the number 1: "))
value2 = int(input("Enter the number 2: "))

print("Random integer between 1 and 10:", random.randint(value1,value2))
print("Random float between 0 and 1:", random.random())