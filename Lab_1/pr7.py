# 7. Write a program to create a dictionary and demonstrate dictionary methods and iteration.
user_information = {}

user_name  = input("Enter Your Name :")
user_age  = input("Enter Your Age :")
user_degree  = input("Enter Your Degree :")
user_information['name']=user_name
user_information['age']=user_age
user_information['degree']=user_degree
print("Full Dictionary = ",user_information)

user_information.pop('age')
print("After Pop Operation = ",user_information)

print("Dictionary Keys = ",user_information.keys())
print("Dictionary Values = " ,user_information.values())

user_information.clear()
print("After Clear Operation = ",user_information)