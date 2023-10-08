from typing import Union
from fastapi import FastAPI, Request
from db import db_create_user, db_get_messages, db_get_user, db_match

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
        "pronouns": "he",
        "interests": "[dsfasdf, asdf, asd, asdf]",
        "location": "golden",
        "events": "[]"
    }
    
    # print(req)
    json = await req.json()
    uid = db_create_user(json)
    return {'user_id': uid}


# Get a user
@app.post("/get_user")
async def get_user(req: Request):
    
    {
        "user_id": "asdfasdf"
    }
    
    json = await req.json()
    print('json', json)
    user = db_get_user(json['user_id'])
    user['_id'] = str(user['_id'])
    print(user)
    return {'user': user}

# Get a match
@app.post("/get_match")
async def get_match(req: Request):
    
    {
        "user_id": "asdfasdf"
    }
    
    json = await req.json()
    print('json', json)
    user = db_match(json['user_id'])
    user['_id'] = str(user['_id'])
    print(user)
    return {'user': user}



### CHAT
# Chat

# Get messages
# Send Message

