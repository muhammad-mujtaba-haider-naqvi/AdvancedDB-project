from pymongo import MongoClient
import os
uri = os.environ.get('MONGO_URI','mongodb://localhost:27017')
print('Connecting to',uri)
client = MongoClient(uri)
for dbname in client.list_database_names():
    db = client[dbname]
    if 'users' in db.list_collection_names():
        count = db.users.count_documents({})
        print(f"{dbname}.users -> {count} documents")
    else:
        # check other collections containing 'user' in name
        for c in db.list_collection_names():
            if 'user' in c.lower():
                print(f"{dbname}.{c} -> {db[c].count_documents({})} documents")
