import os
from pymongo import MongoClient

# Try to load .env if python-dotenv is available (non-fatal)
try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    pass

# Prefer MONGO_URI from env; fall back to localhost for ease of development
MONGO_URI = os.environ.get("MONGO_URI", "mongodb://localhost:27017")

# Optional in-memory mock DB for development/CI when a real MongoDB
# server is not available. Enable by setting USE_MOCK_DB=1 in environment
USE_MOCK = str(os.environ.get("USE_MOCK_DB", "0")).lower() in ("1", "true", "yes")

if USE_MOCK:
    try:
        import mongomock
        client = mongomock.MongoClient()
    except Exception:
        # Fallback to real MongoClient if mongomock isn't installed
        client = MongoClient(MONGO_URI)
else:
    client = MongoClient(MONGO_URI)

db = client.get_database('emotion_db')
emotion_logs = db.get_collection('emotion_logs')
users = db.get_collection('users')
user_memory = db.get_collection('user_memory')

def ping_db():
    try:
        client.admin.command('ping')
        return True
    except Exception:
        return False
