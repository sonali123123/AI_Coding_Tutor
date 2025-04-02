from database import Database

db = Database()
try:
    info = db.client.server_info()
    print("Connected to MongoDB successfully!")
    print(info)
except Exception as e:
    print("Failed to connect to MongoDB:", e)
