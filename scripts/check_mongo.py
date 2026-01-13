import os
from pymongo import MongoClient

uri = os.environ.get('MONGO_URI', 'mongodb://localhost:27017/emotion_db')
print('Using MONGO_URI:', uri)
# derive dbname from uri path if present
dbname = uri.split('/')[-1].split('?')[0] if '/' in uri else 'emotion_db'
if not dbname:
    dbname = 'emotion_db'
print('Derived DB name:', dbname)

client = MongoClient(uri)
db = client[dbname]
print('Collections:', db.list_collection_names())
print('Sample users doc:', db.users.find_one())
print('emotion_logs count:', db.emotion_logs.count_documents({}))
