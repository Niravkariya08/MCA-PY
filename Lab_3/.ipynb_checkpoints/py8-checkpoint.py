# Write a program to demonstrate basic regular expression pattern matching.
import regex

print('--------Regex Operations--------')

userInput = input("Enter a string: ")
reg = '[a-zA-Z]+'

print("The string contains only alphabets:", regex.fullmatch(reg, userInput) is not None)
