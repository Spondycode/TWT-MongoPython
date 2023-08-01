from dotenv import load_dotenv, find_dotenv
import os
import pprint
from pymongo import MongoClient

password = os.environ.get("MONGODB_PWD")

connection_string = f"mongodb+srv://billybongo:{password}@bill.9nr6flq.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(connection_string)
