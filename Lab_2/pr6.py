# 6. Write a program to iterate over lists strings and dictionaries using loops.
lst = [10,20,30,40,50]
string = "Marwadi"
dictionarie = {'name':'Nirav Kariya','eno':'92600584008','branch':'MCA','city':'Gondal'}
i = 0
for i in lst:
    print(i)

for i in string:
    print(i)

for key,value in dictionarie.items():
    print (f"{key} = > {value}")