# Import the db module from replit
import db

# Function to store data in the Replit database
def store_data(key, data):
    db[key] = data

# Function to retrieve data from the Replit database
def get_data(key):
    return db.get(key)

# Example of storing and retrieving data
election_data = {
    "election_name": "General Election 2023",
    "start_date": "2023-01-01",
    "end_date": "2023-12-31"
}

store_data("election_data", election_data)

retrieved_data = get_data("election_data")
print(retrieved_data)