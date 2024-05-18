import sqlite3

def create_database():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS your_table (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        age INTEGER,
                        email TEXT NOT NULL)''')

    conn.commit()
    conn.close()

def insert_record(name, age, email):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO your_table (name, age, email) VALUES (?, ?, ?)", (name, age, email))

    conn.commit()
    conn.close()

def display_records(min_age=None, max_age=None):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    if min_age is not None and max_age is not None:
        cursor.execute("SELECT id, name, age FROM your_table WHERE age >= ? AND age <= ?", (min_age, max_age))
    else:
        cursor.execute("SELECT id, name, age FROM your_table")

    records = cursor.fetchall()

    if records:
        print("ID\tName\tAge")
        for record in records:
            print(f"{record[0]}\t{record[1]}\t{record[2]}")
    else:
        print("No records found in the database.")

    conn.close()

create_database()


insert_record("Anna", 33, "anna@gmail.com")
insert_record("Andrii", 15, "andrii@gmail.com")
insert_record("Mike", 47, "mike@gmail.com")

min_age = input("Enter the minimum age: ")
max_age = input("Enter the maximum age: ")

if min_age:
    min_age = int(min_age)
if max_age:
    max_age = int(max_age)

display_records(min_age, max_age)
