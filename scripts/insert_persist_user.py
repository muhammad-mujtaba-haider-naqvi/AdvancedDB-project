from pymongo import MongoClient
import os
uri = os.environ.get('MONGO_URI','mongodb://localhost:27017/emotion_db')
print('Connecting to',uri)
client = MongoClient(uri)
# derive db name
dbname = uri.split('/')[-1].split('?')[0] or 'emotion_db'
db = client[dbname]
user = {'user_id':'persist_test','name':'Persistent User'}
res = db.users.replace_one({'user_id':user['user_id']}, user, upsert=True)
print('replace_one result matched_count', getattr(res,'matched_count',None),'upserted_id', getattr(res,'upserted_id',None))
print('Now collections:', db.list_collection_names())
print('users count:', db.users.count_documents({}))
print('sample:', db.users.find_one({'user_id':'persist_test'}))
