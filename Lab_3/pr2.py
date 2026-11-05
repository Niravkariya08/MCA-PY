# 2. Write a program to demonstrate different import mechanisms in Python. 
from calculator import add
print(add(10,5))

import calculator as calculator 
print(calculator.sub(10,5))

from calculator import *
print(add(10,20))

import calculator as c
print(c.add(10,20))