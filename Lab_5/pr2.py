def divide_numbers(a, b):
    try:
        result = a / b
        
    except ZeroDivisionError:
        print("Error: You cannot divide a number by zero!")
        
    else:
        print(f"Success! The result is {result}")
        
    finally:
        print("Done executing the try-except-else-finally structure.\n")

print("--- Test 1: Valid input ---")
divide_numbers(10, 2)

print("--- Test 2: Invalid input ---")
divide_numbers(10, 0)