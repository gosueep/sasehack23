from typing import Union
from fastapi import FastAPI

# from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi
# uri = "mongodb+srv://mongo:IU1vQmHaqMbox24D@sase.tktciax.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp"
# # Create a new client and connect to the server
# client = MongoClient(uri, server_api=ServerApi('1'))

from pymongo import MongoClient
def get_database():
 
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   CONNECTION_STRING = "mongodb+srv://mongo:IU1vQmHaqMbox24D@sase.tktciax.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp"
 
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient(CONNECTION_STRING)
 
   # Create the database for our example (we will use the same database throughout the tutorial
   return client['peopler']
  
db = get_database()
print(db)
print(db["people"])
for item in db["people"].find():
    print(item)

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
