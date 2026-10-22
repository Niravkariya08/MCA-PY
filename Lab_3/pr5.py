#Write a program to display current date and time using date time module. 

import datetime

print("Current date and time:", datetime.datetime.now())
print("Current date:", datetime.date.today().strftime("%d/%m/%Y"))
print("Current time:", datetime.datetime.now().time())
print("Current year:", datetime.datetime.now().year)
print("Current month:", datetime.datetime.now().month)
