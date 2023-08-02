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


# function to insert one document
def insert_test_doc():
    collection = test_db.test
    test_document = {"name": "David", "type": "test"}
    inserted_id = collection.insert_one(test_document).inserted_id
    print(inserted_id)


production = client.production
person_collection = production.person_collection


# Function to insert many documents
def create_documents():
    first_names = [
        "Tim",
        "Sarah",
        "Jennifer",
        "Jose",
        "Pit",
    ]
    last_names = ["Allen", "Smith", "Bart", "Cater", "Geral"]
    ages = [21, 40, 19, 34, 67]
    # Create empty list
    docs = []
    # Loop though the three list using the zip function.
    for first_name, last_name, age in zip(first_names, last_names, ages):
        doc = {"first_name": first_name, "last_name": last_name, "age": age}
        docs.append(doc)

    person_collection.insert_many(docs)


printer = pprint.PrettyPrinter()
# Two previous functions were creating documents in the collection -

# Next is to get docs from the database


# Creating Documents in our new collection
def find_all_people():
    people = person_collection.find()

    for person in people:
        printer.pprint(person)


def find_Sarah():
    sara = person_collection.find_one({"first_name": "Sarah"})
    printer.pprint(sara)


# Find a person by ID
def get_person_by_id(person_id):
    from bson.objectid import ObjectId

    _id = ObjectId(person_id)
    person = person_collection.find_one({"_id": _id})
    printer.pprint(person)


def get_age_range(min, max):
    query = {"$and": [{"age": {"$gte": min}}, {"age": {"$lte": max}}]}

    people = person_collection.find(query).sort("age")
    for person in people:
        printer.pprint(person)


get_age_range(20, 35)
