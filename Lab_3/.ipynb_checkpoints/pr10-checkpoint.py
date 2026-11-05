#Write a program to extract specific information from a text file using regular expressions.
import re

email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

with open("data.txt", "r") as file:
    content = file.read()
    emails = re.findall(email_pattern, content)

print("Found emails:", emails)
