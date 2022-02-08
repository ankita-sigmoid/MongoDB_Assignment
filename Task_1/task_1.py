import pymongo

print('Q1. Create a Python application to connect to MongoDB.')
try:
    # Format - (protocol://IP address:port/)
    client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
    print('Connection was successful!')

except:
    print('Sorry, we were unable to establish your connection.')
