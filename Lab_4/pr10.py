filename = "sample.txt"

with open(filename, "w") as file:
    file.write("Hello, Python!")

with open(filename, "r") as file:
    
    print("Initial position:", file.tell())  
    
    print("Read first 5 chars:", file.read(5))  
    
    print("Position after reading 5 chars:", file.tell())  
    
    file.seek(7)  
    print("\nPosition after seek(7):", file.tell())  
    
    print("Read remaining chars:", file.read())