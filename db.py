from pymongo import MongoClient
def get_database():
 
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   CONNECTION_STRING = "mongodb+srv://mongo:IU1vQmHaqMbox24D@sase.tktciax.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp"
 
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient(CONNECTION_STRING)
 
   # Create the database for our example (we will use the same database throughout the tutorial
   return client['Peopler']


def db_create_user(user):
    db["people"].insert_one(user)
    
    

if __name__ == "__main__":
    db = get_database()
    print(db)
    print(db["people"].find_one())
    for item in db["people"].find():
        print(item)
        
    
    db_create_user({
        "test": "asda"
    })
    
    
