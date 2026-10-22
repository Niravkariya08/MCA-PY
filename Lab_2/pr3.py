#  3.Write a program to generate a multiplication table using a for loop. 
num1 = int(input("Enter Number :"))
i=0
for i in range(1,11):
    print(f"{num1} * {i} = ",num1*i)