
def serialize(data):
    import pickle
    with open('data.pickle', 'wb') as file:
        pickle.dump(data, file)
    with open('data.pickle', 'rb') as file:
        serialized_data = file.read()
    return serialized_data

def connect():
    import sqlite3
    connection = sqlite3.connect("mydatabase.db")
    cursor = connection.cursor()
    return connection, cursor

def create_table(conn):
    import sqlite3
        # Create a cursor object
    cursor = conn.cursor()
        # Define the table with 7 columns
    try:
        cursor.execute('''CREATE TABLE data (
                            id INTEGER PRIMARY KEY,
                            sets BLOB)''')
        # Commit the changes to the database
        conn.commit()
    except sqlite3.OperationalError:
        pass
        # Close the connection

def has_table(cursor, table_name):
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
    return bool(cursor.fetchone())
    

def commit_to_table(conn, data):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO data (sets) VALUES (?)", (data,))
    conn.commit()
    return print("Commit successful.")

def get_last_set(cursor, table_name):
    cursor.execute(f"SELECT * FROM {table_name}")
    row = cursor.fetchone()
    return row

def get_all_sets(cursor, table_name):
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    return rows

