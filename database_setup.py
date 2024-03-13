import sqlite3

# Connect to SQLite database (or create if it doesn't exist)
conn = sqlite3.connect("charts.db")
c = conn.cursor()

# Create a table to store chart data
c.execute('''CREATE TABLE IF NOT EXISTS charts (
                id INTEGER PRIMARY KEY,
                patient_name TEXT,
                age INTEGER,
                symptoms TEXT
             )''')

# Commit changes and close connection
conn.commit()
conn.close()
