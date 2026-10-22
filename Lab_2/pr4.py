# 4.Write a program to find the sum of digits of a number using a while loop.

#While
num1 = input("Enter Number :")
sum = 0
i = 0

while i < len(num1):
    typecast = int(num1[i])
    sum += typecast
    i += 1

print(sum)


#For Loop
num1 = input("Enter Number :")
sum = 0
for i in num1:
    typecast = int(i)
    sum+=typecast

print(sum)