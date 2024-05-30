import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('example.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Create a table named 'products'
cursor.execute('''CREATE TABLE IF NOT EXISTS products 
                (id INTEGER PRIMARY KEY, name TEXT, description TEXT)''')

# Check if the 'image' column exists, and add it if it doesn't
cursor.execute("PRAGMA table_info(products)")
columns = [col[1] for col in cursor.fetchall()]
if 'image' not in columns:
    cursor.execute('''ALTER TABLE products ADD COLUMN image TEXT''')

# Clear all existing records from the 'products' table
cursor.execute("DELETE FROM products")

# Insert some sample data into the 'products' table
cursor.execute("INSERT INTO products (name, description, image) VALUES (?, ?, ?)", ('Bolo', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. ', 'https://img.freepik.com/psd-gratuitas/bolo-derramado-com-chocolate-e-decorado-com-diferentes-biscoitos-em-um-fundo-transparente_84443-1736.jpg?t=st=1716933898~exp=1716937498~hmac=5f18c4b9bf0d1f005b979b3b215f12e3f0585a2f421efe3ee05697f4b5e6c4fe&w=740'))
cursor.execute("INSERT INTO products (name, description, image) VALUES (?, ?, ?)", ('Sanduiche', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. ', 'https://img.freepik.com/psd-premium/saborosa-fatia-de-sanduiche-de-presunto-e-queijo-isolada-em-fundo-transparente_927015-1493.jpg?w=996'))
cursor.execute("INSERT INTO products (name, description, image) VALUES (?, ?, ?)", ('Torta', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. ', 'https://img.freepik.com/fotos-gratis/posicao-plana-de-torta-de-abobora-de-acao-de-gracas_23-2148686215.jpg?t=st=1716934004~exp=1716937604~hmac=848ca57497674d54bd90653d9c8c8feff339e0eea16044538385c8c7107bf01c&w=740'))
cursor.execute("INSERT INTO products (name, description, image) VALUES (?, ?, ?)", ('Nuggets', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. ', 'https://img.freepik.com/fotos-gratis/nuggets-de-frango-com-molho-barbecue-na-mesa_140725-6556.jpg?t=st=1716935287~exp=1716938887~hmac=b470f7d793918609733c91a9059e6da664f46783a2002852805b182cdac7eb4e&w=740'))

# Commit changes and close the connection
conn.commit()
conn.close()
