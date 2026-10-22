# 4. Write a program to demonstrate string operations including slicing formatting and built-in string functions.
user_input = input("Enter a String Here :  ")

print("\n--Slicing Operation--")
print(user_input[0:3])
print(user_input[0:5:2])
print(user_input[::-1])

print("\n--Formating Operation--")
name = "Nirav"
age = 21
city = "Gondal"
print(f"Hello,Good Morning my name is {name} i am {age} years old and i am from {city} city")


print("Built in String Function")
print(user_input.upper())
print(user_input.lower())
print(user_input.find("a"))
print(user_input.count("a"))
print(user_input.replace("a","xyz"))
print(user_input.split(" "))