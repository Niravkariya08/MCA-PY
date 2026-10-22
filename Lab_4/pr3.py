#Write a program to illustrate instance variables and class variables. 
class printUserInfo : 
    clg = "Marwadi University"  #class variable

    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
    
    def print_info(self):
        print(f"College: {self.clg}")
        print(f"\nName: {self.name}")
        print(f"Age: {self.age}")
        print(f"City: {self.city}")
        
s1 = printUserInfo('Nirav', 21, 'Gondal')    
s1.print_info()   

s2 = printUserInfo('John', 25, 'New York')    
s2.print_info()   