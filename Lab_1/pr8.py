# 8. Write a program to explain mutable and immutable objects in Python. 
lst = [1, 2, 3]

lst.append(4)
print(lst)      # Output: [1, 2, 3, 4]

lst = (1,2,3)
#tuple is Immutable that have no add or append method 