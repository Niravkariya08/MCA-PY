filename = "data.txt"

with open(filename, 'w') as file:
    file.write("Hello! This is the first line.\n")
print("Data written successfully.")

with open(filename, 'a') as file:
    file.write("This line is appended.\n")
print("Data appended successfully.")

print("\n--- Reading File Contents ---")
with open(filename, 'r') as file:
    content = file.read()
    print(content)