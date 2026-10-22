#Write a program to demonstrate instance methods class methods and static methods. 
class printUserInfo : 
    clg = "Marwadi University"  #class variable
    result = ''
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
    
    def print_info(self):
        print(f"\nName: {self.name}")
        print(f"Age: {self.age}")
        print(f"City: {self.city}")
        
    @classmethod    
    def UserResult(cls,sub1,sub2,sub3):
        global Result
        result = 'Pass' if(sub1+sub2+sub3)/3 >= 40  else 'Fail'
        percentage = ((sub1+sub2+sub3)/300)*100
        print("\n----------Student Result----------")
        print(f"Subject 1: {sub1}")
        print(f"Subject 2: {sub2}")
        print(f"Subject 3: {sub3}")
        print('Sum of marks:',sub1+sub2+sub3)
        print('Percentage of marks:',f'{percentage:.2f}%')
        print('Result:',result)
        print('----------------------------------')
        print(f'{'Congo' if result == 'Pass' else 'we are sorry'}' )
        print('----------------------------------')
        
    @staticmethod
    def UserInfo():
        print("This is a static method")
        
    print("Welcome to", clg)

        
s1 = printUserInfo('Nirav', 21, 'Gondal')    
s1.print_info()   
s1.UserResult(10, 8, 7)