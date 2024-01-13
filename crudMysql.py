#Ejecute antes pip install mysql-connector-python

import mysql.connector

# Database configuration
config = {
    'user': 'your_username',
    'password': 'your_password',
    'host': 'localhost',
    'database': 'your_database',
    'raise_on_warnings': True
}

# Establish a database connection
conn = mysql.connector.connect(**config)
cursor = conn.cursor()

# CREATE operation - creating a new table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL
)
""")
print("Table created.")

# INSERT operation - adding data to the table
add_user = ("INSERT INTO users (username, email) "
            "VALUES (%s, %s)")
data_user = ('john_doe', 'john.doe@example.com')
cursor.execute(add_user, data_user)
conn.commit()
print("User added.")

# READ operation - querying data from the table
query = "SELECT id, username, email FROM users"
cursor.execute(query)

for (id, username, email) in cursor:
    print(f"ID: {id}, Username: {username}, Email: {email}")

# UPDATE operation - updating data in the table
update_user = ("UPDATE users SET email = %s WHERE id = %s")
data_update = ('john.newemail@example.com', 1)
cursor.execute(update_user, data_update)
conn.commit()
print("User updated.")

# DELETE operation - deleting data from the table
delete_user = ("DELETE FROM users WHERE id = %s")
data_delete = (1,)
cursor.execute(delete_user, data_delete)
conn.commit()
print("User deleted.")

# Close the cursor and the connection
cursor.close()
conn.close()
