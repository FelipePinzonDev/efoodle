from pymongo import MongoClient
from dotenv import load_dotenv
import os
# Load environment variables from .env file
BASE_URI = os.getenv("BASE_URI")

load_dotenv()

client = MongoClient(BASE_URI)

db = client.efoodle_db

food_collection = db["food"]
drinks_collection = db["drinks"]
desserts_collection = db["desserts"]
combo_collection = db["combos"]