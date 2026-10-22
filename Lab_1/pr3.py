# 3. Write a program to perform arithmetic relational and logical operations using Python operators.
num1 = int(input("Enter 1 Number : "))
num2 = int(input("Enter 2 Number : "))
num3 = int(input("Enter 3 Number : "))

print("\n--Arithmetic operation--")
print(f"Sum of {num1} + {num2} : {num1+num2}")
print(f"Sub of {num1} - {num2} : {num1-num2}")
print(f"Mul of {num1} * {num2} : {num1*num2}")
print(f"Div of {num1} / {num2} : {num1/num2}\n")

print("--Relational operation--")
print(f"{num1} is greater than {num2} : {num1>num2}")
print(f"{num2} is greater than {num1} : {num1<num2}")

print("\n--Logical operation--")
print(f"{num1} is greater than {num2} and {num1} is greater than {num3} : {num1 > num2 and num1 > num3}")
print(f"{num1} is greater than {num2} and {num1} is greater than {num3} : {num1 < num2 or num1 > num3}")