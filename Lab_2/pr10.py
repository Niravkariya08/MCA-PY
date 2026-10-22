# 10.Write a program to generate a sequence of numbers using generator functions and yield keyword.
def count_up_to(max_value):
    count = 1
    while count <= max_value:
        yield count
        count += 1

counter = count_up_to(3)

print(next(counter)) 
print(next(counter)) 
print(next(counter))