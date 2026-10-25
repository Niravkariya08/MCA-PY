### Write a program to demonstrate method overriding and polymorphism. 

class A:
    def display(self):
        print("This is class A")

class B(A):
    def display(self):
        super().display()
        print("This is class B")
    
class C(B):
    def display(self):
        super().display()
        print("This is class C")
        
obj = C()
obj.display()