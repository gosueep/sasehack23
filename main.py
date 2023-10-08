from typing import Union
from fastapi import FastAPI, Request
from db import db_create_user, db_get_messages, db_get_user, db_match, db_chat_screen

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


# Get a match
@app.post("/get_match")
async def get_match(req: Request):
    
    {
        "name": "asdfasdf",
        "pronouns": "he",
        "interests": "[dsfasdf, asdf, asd, asdf]",
        "location": "golden",
        "events": "[]"
    }
    
    json = await req.json()
    print('json', json)
    user = db_match(json['user_id'])
    user['_id'] = str(user['_id'])
    print(user)
    return {'user': user}



### CHAT
# Chat

texts = []

@app.post("/send_message")
async def send_message(req: Request):
    json = await req.json()             #will be a request to send a message
    message = json.get("message")
    
    if message:
        texts.append({"sender": "You (The person writing the messaeg)", "message": message})    #the message will be appeneded to the texts array
        return {"message": "Delivered"}     #if there is a message
    else:
        return {"message": "Empty"}         #if there is no message

#will be used to look at past messages taht are stored into texts
@app.get("/receive_messages")
def receive_messages():
    return texts
# Get messages
# Send Message

