import sqlite3
conn = sqlite3.connect('people.db')# Add the name of your database inside the quotes
cursor = conn.cursor()
### Add SQL to define your table inside the quotes below
cursor.execute('''
                      CREATE TABLE IF NOT EXISTS users (
                      user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                      username TEXT,
                      password TEXT,
                      auth_level INTEGER
               )
                ''')
conn.commit()
conn.close()
# Add the name of your database in the quotes below
print("Database '' created successfully.")