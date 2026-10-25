#Write a program to use re module functions such as match search and find all. 
import re

text = "Python is fun, python is powerful, and Python rules!"
pattern = r"Python" 

match_result = re.match(pattern, text)
print(f"Match: {match_result.group()}")

text_two = "I love Python programming!"
search_result = re.search(pattern, text_two)
print(f"Search: {search_result.group()}")

findall_result = re.findall(pattern, text)
print(f"Findall: {findall_result}")
