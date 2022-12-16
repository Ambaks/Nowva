
 


def create_table():
    import sqlite3
    conn = sqlite3.connect('userData.db')
        # Create a cursor object
    cursor = conn.cursor()
        # Define the table with 7 columns
    cursor.execute('''CREATE TABLE data (
                        id INTEGER PRIMARY KEY,
                        sets BLOB)''')
        # Commit the changes to the database
    conn.commit()
        # Close the connection
    

def commit_to_table(set):
    import sqlite3
    import pickle

    conn = sqlite3.connect('userData.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='data'")

    if cursor.fetchone():
        with open('data.pickle', 'wb') as file:
            data = pickle.dump(set, file)
        cursor.execute('INSERT INTO data (sets)  VALUES (?)', (data))
        conn.commit()
        conn.close()
    else:
        with open('data.pickle', 'wb') as file:
            data = pickle.dump(set, file)
            create_table()
        cursor.execute('INSERT INTO data (sets)  VALUES (?)', (data))
        conn.commit()
        conn.close()

