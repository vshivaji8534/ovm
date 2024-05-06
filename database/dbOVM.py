import sqlite3

# Create a connection to the database
conn = sqlite3.connect('voting_database.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Create a table to store vote casting information
cursor.execute('''
    CREATE TABLE IF NOT EXISTS votes (
        id INTEGER PRIMARY KEY,
        user_id TEXT,
        candidate TEXT,
        constituency TEXT,
        election_type TEXT
    )
''')

# Function to insert a new vote casting record into the database
def insert_vote(user_id, candidate, constituency, election_type):
    cursor.execute('''
        INSERT INTO votes (user_id, candidate, constituency, election_type)
        VALUES (?, ?, ?, ?)
    ''', (user_id, candidate, constituency, election_type))
    conn.commit()

# Function to retrieve all vote casting records from the database
def get_all_votes():
    cursor.execute('''
        SELECT * FROM votes
    ''')
    return cursor.fetchall()

# Close the database connection
conn.close()