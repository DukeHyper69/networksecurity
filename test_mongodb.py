import sys
from pymongo.mongo_client import MongoClient
from networksecurity.exception.exception import NetworkSecurityException

uri = "mongodb+srv://kaaljung099_db_user:Admin123@cluster0.zmfz6yc.mongodb.net/?appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    raise NetworkSecurityException(e,sys)