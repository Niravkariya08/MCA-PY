# 8. Write a program to illustrate variable scope using local global and nonlocal variables.
user_data = "Abc Univerity"

def adminlogin():
    admin_name = "admin@08"
    print(admin_name) #admin@08
    global user_data  
    user_data = "Abc#University"
    print(user_data) #Abc Univerity
    
adminlogin()

#print(admin_name) here admin name was not print because of local variable of adminlogin function 


def outer_func():
    count = 0
    
    def inner_func():
        count = 5 
        print("Inner count:", count)
        
    inner_func()
    print("Outer count:", count)

outer_func()
# Outer count: 0  <-- The original outer variable was never updated!