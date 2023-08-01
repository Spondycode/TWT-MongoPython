from dotenv import load_dotenv, find_dotenv
import os
import pprint  # Just for using with the test - not for the final app.
from pymongo import MongoClient

load_dotenv(find_dotenv())
# Getting the password from the .env file
password = os.environ.get("MONGODB_PWD")

# Connecting to MongoDB
connection_string = f"mongodb+srv://billybongo:{password}@bill.9nr6flq.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connection_string)

# Proving the connection to the database
dbs = client.list_database_names()
test_db = client.test
collections = test_db.list_collection_names()
print(collections)
