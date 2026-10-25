#Write a program to illustrate method resolution order and magic methods. 

class A:
    def greet(self): 
        print("Hello from A")

class B:
    def greet(self): 
        print("Hello from B")

class Child(A, B): 
    pass

class Toy:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Toy: {self.name}"

c = Child()
c.greet()

t = Toy("Car")
print(t)
