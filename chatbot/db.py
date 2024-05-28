import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('example.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Create a table named 'products'
cursor.execute('''CREATE TABLE IF NOT EXISTS products 
                (id INTEGER PRIMARY KEY, name TEXT, description TEXT)''')

# Insert some sample data into the 'products' table
cursor.execute("INSERT INTO products (name, description) VALUES (?, ?)", ('Bolo', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. '))
cursor.execute("INSERT INTO products (name, description) VALUES (?, ?)", ('Sanduiche', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. '))
cursor.execute("INSERT INTO products (name, description) VALUES (?, ?)", ('Torta', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. '))

# Commit changes and close the connection
conn.commit()
conn.close()
