# 5. Write a program to create and manipulate lists using indexing slicing and list comprehensions. 
user_info = []
user_info.clear()
user_name = input("Enter Your Name :")
user_info.append(user_name)

user_age = int(input("Enter Your Age :"))
user_info.append(user_age)

user_city = input("Enter Your city :")
user_info.append(user_city)

print('--Full List--',user_info)
print('--Index Slicing--',user_info[0:2])


numbers = [1,2,3,4,5,6,7,8,9,10]
squares = []

for i in numbers:
    squares.append(i ** 2)
print(numbers)
print(squares)