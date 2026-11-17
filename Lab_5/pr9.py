import mysql.connector

# mydb = mysql.connector.connect(
# host="localhost",
# user="root",
# password=""
# )
# print(mydb)

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mca_4008"
)

cursor = db_connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        department VARCHAR(255),
        salary INT
    )
''')

insert_query = "INSERT INTO employees (name, department, salary) VALUES (%s, %s, %s)"
values = [
    ("Nirav", "HR", 50000),
    ("Ansh", "IT", 75000)
]
cursor.executemany(insert_query, values)
db_connection.commit() 
print(f"{cursor.rowcount} record(s) inserted successfully.\n")

cursor.execute("SELECT * FROM employees")
records = cursor.fetchall()

print("--- Employee Records from phpMyAdmin ---")
for row in records:
    print(f"ID: {row[0]} | Name: {row[1]} | Dept: {row[2]} | Salary: ${row[3]}")

cursor.close()
db_connection.close()