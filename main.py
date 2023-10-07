from typing import Union
from fastapi import FastAPI, Request

from pymongo import MongoClient
def get_database():
 
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   CONNECTION_STRING = "mongodb+srv://mongo:IU1vQmHaqMbox24D@sase.tktciax.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp"
 
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient(CONNECTION_STRING)
 
   # Create the database for our example (we will use the same database throughout the tutorial
   return client['Peopler']
  
db = get_database()
print(db)
print(db["people"].find_one())
for item in db["people"].find():
    print(item)



##############
## API
##############

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


# Create User Interests to User
# add event
@app.post("/create_user")
async def create_user(req: Request):
    
    {
        "name": "asdfasdf",
        "interests": "[dsfasdf, asdf, asd, asdf]",
        "location": "golden",
        "events": "[]"
    }
    
    
    print(req)
    return await req.json()


# Get a match


### CHAT
# Chat

# Get messages
# Send Message

