import sqlite3

connection = sqlite3.connect('database.db')
with open('app/database/schema.sql') as f:
    connection.executescript(f.read())

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn
