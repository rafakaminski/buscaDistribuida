from pymongo import MongoClient
import time


def wait_for_mongo(uri, timeout=60):
    client = MongoClient(uri)
    start_time = time.time()
    while True:
        try:
            client.admin.command('ping')
            print("MongoDB is available")
            return True
        except Exception as e:
            print(f"Waiting for MongoDB... {e}")
            time.sleep(2)
            if time.time() - start_time > timeout:
                print("Timeout waiting for MongoDB")
                return False
            

def initialize_database(uri, db_name, data):
    client = MongoClient(uri)
    db = client[db_name]
    collection = db["listingsAndReviews"]
    collection.insert_many(data)
    

if wait_for_mongo("mongodb://mongodb:27017"):
    data_api_1 = [
        {"_id": "101", "name": "Item 101", "description": "Descrição do item 101"},
        {"_id": "102", "name": "Item 102", "description": "Descrição do item 102"},
        {"_id": "103", "name": "Item 103", "description": "Descrição do item 103"},
        {"_id": "104", "name": "Item 104", "description": "Descrição do item 104"}
    ]
    

    data_api_2 = [
        {"_id": "201", "name": "Item 201", "description": "Descricao do Item 201"},
        {"_id": "202", "name": "Item 202", "description": "Descricao do Item 202"},
        {"_id": "203", "name": "Item 203", "description": "Descricao do Item 203"},
        {"_id": "204", "name": "Item 204", "description": "Descricao do Item 204"}
    ]


    data_api_3 = [
        {"_id": "301", "name": "Item 301", "description": "Descrição do Item 301"},
        {"_id": "302", "name": "Item 302", "description": "Descrição do Item 302"},
        {"_id": "303", "name": "Item 303", "description": "Descrição do Item 303"},
        {"_id": "304", "name": "Item 304", "description": "Descrição do Item 304"}
    ]


    initialize_database("mongodb://mongodb:27017", "api_1_db", data_api_1)
    initialize_database("mongodb://mongodb:27017", "api_2_db", data_api_2)
    initialize_database("mongodb://mongodb:27017", "api_3_db", data_api_3)

    print("Databases initialized successfully.")
else:
    print("Failed to connect to MongoDB within the timeout period.")