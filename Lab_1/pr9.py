# 9.Write a program to define and use user-defined functions with different types of arguments.
def userData (num1,num2):   #positional argument
    return num1+num2

addition = userData(10,20)
print(addition)


def userInfo (degree,name = 'Nirav'):  #defualt argument 
    print(f'Hello {name} you are {degree} Student.')

userInfo('MCA')


def user1(name,*marks):  #Veriable Length Argument
    print(f'User {name} have {marks} marks in Exam')

user1('Nirav',12,20,30,40,50)

result = userData(num2=25,num1=8)  #Keyword Argument
print(result)