import mysql.connector

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mca_4008"
)
cursor = db_connection.cursor()

cursor.execute("CREATE TABLE employees (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50))")

names = [("Nirav",), ("Ansh",), ("Shyam",), ("Om",), ("Rahul",), ("Priyam",)]
cursor.executemany("INSERT INTO employees (name) VALUES (%s)", names)
db_connection.commit()

cursor.execute("SELECT * FROM employees")

# 1. fetchone(): First row
print("--- 1. Using fetchone() ---")
row1 = cursor.fetchone()
print(row1)  


# 2. fetchmany(size): Retrieves Record 2 and 3
print("\n--- 2. Using fetchmany(2) ---")
rows2_and_3 = cursor.fetchmany(2)
for row in rows2_and_3:
    print(row)  


# 5. fetchall(): Retrieves all remaining rows (Records 4, 5, and 6)
print("\n--- 3. Using fetchall() ---")
remaining_rows = cursor.fetchall()
for row in remaining_rows:
    print(row)  

cursor.close()
db_connection.close()