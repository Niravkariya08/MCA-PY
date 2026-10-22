# 2. Write a program to demonstrate different import mechanisms in Python. 
from Lab_3.calculator import add
print(add(10,5))

import Lab_3.calculator as calculator 
print(calculator.sub(10,5))

from Lab_3.calculator import *
print(add(10,20))

import Lab_3.calculator as c
print(c.add(10,20))