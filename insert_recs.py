import sqlite3
from users import users_data

conn = sqlite3.connect('people.db') # Insert the name of your database inside the quotes
cursor = conn.cursor()

for user in users_data:
    #cursor.execute("INSERT INTO fertilizers (brand, price, type) VALUES (?, ?, ?)", (fertilizer['brand'], fertilizer['price'], fertilizer['type']))
    # create a similar line of code to the above line insert the user INSTEAD of fertilizer data into the users table
    sql_query = "INSERT INTO users (user_id, username, password, auth_level) VALUES (?, ?, ?, ?)"
    value = (user['user_id'], user['username'], user['password'], user['auth_level'])
    cursor.execute(sql_query, value)
conn.commit()
conn.close()

print("Data inserted successfully.")
