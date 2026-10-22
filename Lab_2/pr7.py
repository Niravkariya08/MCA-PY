# 7. Write a program to demonstrate list dictionary and set comprehensions.
lst = [10,20,30,40]
lst_output = [i**2 for i in lst]
print(lst_output)

dictionarie_output = {i:i**3 for i in lst}
print(dictionarie_output)

set_output = {i%20 == 0 for i in lst }
print(set_output)