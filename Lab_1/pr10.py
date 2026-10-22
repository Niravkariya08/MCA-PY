# 10.Write a program to demonstrate recursion using factorial or Fibonacci series.
def factorial_recursive(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n < 2:
        return 1
    
    return n * factorial_recursive(n - 1)

user_input = int(input('Enter Number :'))
print(factorial_recursive(user_input))