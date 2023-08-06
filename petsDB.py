import mysql.connector
import os
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

conn = mysql.connector.connect(
    host=config.get('mysql', 'host'),
    user=config.get('mysql', 'user'),
    password=config.get('mysql', 'password'),
    database=config.get('mysql', 'database')
)

# Use a BufferedCursor instead
cursor = conn.cursor(buffered=True)

# If you want to see the records before inserting new data, fetch and print them here:
cursor.execute("SELECT * FROM animals")
rows_before = cursor.fetchall()
print("Before inserting:")
for row in rows_before:
    print(row)

# Inserting the new record
cursor.execute("""
INSERT INTO animals (name, species) VALUES ('Buddy', 'dog');
""")
conn.commit()  # Committing the transaction

# Fetch and print all records after the insert
cursor.execute("SELECT * FROM animals")
rows_after = cursor.fetchall()
print("After inserting:")
for row in rows_after:
    print(row)

cursor.close()
conn.close()

