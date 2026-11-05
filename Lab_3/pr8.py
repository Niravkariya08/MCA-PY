# Write a program to demonstrate basic regular expression pattern matching.
import re

print('--------Regex Operations--------')

userInput = input("Enter a string: ")
reg = '[a-zA-Z]+'

print("The string contains only alphabets:", re.fullmatch(reg, userInput) is not None)
