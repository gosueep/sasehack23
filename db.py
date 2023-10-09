import random
from bson.objectid import ObjectId
from pymongo import MongoClient

import openai

import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())


def get_database():
 
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   CONNECTION_STRING = f'mongodb+srv://mongo:{os.getenv("db_pass")}@sase.tktciax.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp'
 
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient(CONNECTION_STRING)
 
   # Create the database for our example (we will use the same database throughout the tutorial
   return client['Peopler']

db = get_database()


# {
#     "name": "asdfasdf",
#     "interests": "[dsfasdf, asdf, asd, asdf]",
#     "location": "golden",
#     "events": "[]"
# }
def db_create_user(user):
    # print('user', user)
    user_id = db["people"].insert_one(user).inserted_id
    return str(user_id)     # MAKE SURE TO CAST TO A STRING



def db_get_user(userID):
    user = db["people"].find_one({"_id": ObjectId(userID)})
    return user

def db_match(userID):    
    user = db_get_user(userID)
    print(user)
    
    matches = []
    for person in db["people"].find():
        if user['hobbies'] != person['hobbies']:
            continue
        for i in user['hobbies']:
            # if "asdf" in ["asdf", "ab"]
            if i in person['hobbies']:
                matches.append(person)
    
    return matches[random.randrange(0,len(matches))]
                

# {
#     "sender": "SENDER_ID",
#     "recipient": "REC_ID",
#     "msg": "TEST MESSAGE"
# }
def db_get_messages(senderID, recipientID):
    sent = db["chat"].find({"sender": senderID, "recipient": recipientID})
    rec = db["chat"].find({"sender": recipientID, "recipient": senderID})
    for i in sent:
        print(i)
    for i in rec:
        print(i)
    
    return sent, rec
    


if __name__ == "__main__":
    print(db)
    # print(db["people"].find_one())
    # for item in db["people"].find():
    #     print(item)
    
    
    # users=[{
    #     "name": "Bob",
    #     "interests": ['yoga', 'kdramas', 'video games'],
    #     "location": "golden",
    #     "events": []
    # },
    #        {
    #     "name": "Joe",
    #     "interests": ['yoga', 'kdramas', 'video games'],
    #     "location": "golden",
    #     "events": []
    # }
    # ]
    # db_create_user(users[1])
       
    db_get_messages(1234, 4321)
    
    x = db_match('652222b4841773d5f3a7d98d')
    print(x)
    
    
#this is the ai that will create suggestions on what to0 say
def generate_suggestion(prompt):
    response = openai.chat_Completion.create(
        engine="text-davinci-002",  # Will use this engine because its created for the purpose of language generation
        prompt=prompt,
        max_tokens=20,  # I feel like 20 is enough
        temperature=0.5,  # This is just how creative the responses will be, max will be 1
    )
    return response.choices[0].text.strip()