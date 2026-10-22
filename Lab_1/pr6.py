# 6. Write a program to illustrate the use of tuples and sets with basic operations.
print('--Tuple--')
user_details = ('Nirav',21,'MCA',21,22)
print(user_details.count(21))
print(user_details[2])

print('\n--Set--')
s1 = {'Nirav',21,'Gondal'}
user_edu = input('Enter Your Qualification :')
s1.add(user_edu)
print(s1)