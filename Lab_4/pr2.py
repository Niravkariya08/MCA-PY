#Write a program to demonstrate constructor and destructor usage.
class printUserInfo :   #Class Declaration 
    
    def print_info(self):
        print("Name: Nirav")
        print("Age: 21")
        print("City: Gondal")
    
    # this method is called when the object is created || Call First then after other methods are called
    def __init__(self):
        print("Constructor is called first")
        
    def __del__(self):
        print("Destructor is called last") #this method have no need to call explicitly, it is called automatically when the object is destroyed.
        
s1 = printUserInfo()    #class object create 
s1.print_info()   