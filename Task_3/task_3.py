import pymongo
from pprint import pprint
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

# Task 3
movies = client.mflix3.movies
comments = client.mflix3.comments
theaters = client.mflix3.theaters
users = client.mflix3.users

new_movie = {
    "plot": "Slice of Life",
    "genres": ["dark", "supernatural"],
    "title": "shut"
}

new_comment = {
    "name": "Aman Sharma",
    "text": "Dying to win and risking death to win is completely different.",
}

new_theater = {
    "theater_id": 73,
    "location": {
        "address": {
            "city": "village hidden in leaf"
        }
    }
}

new_user = {
    "name": "Draken",
    "email": "delinquent@sloppy.world.com",
    "password": "asIfIWillTellYa"
}

# Insertion
new_movie_id = movies.insert_one(new_movie).inserted_id
new_comment_id = comments.insert_one(new_comment).inserted_id
new_theater_id = theaters.insert_one(new_theater).inserted_id
new_user_id = users.insert_one(new_user).inserted_id

# Fetching new documents
movie = movies.find_one({"_id": new_movie_id})
comment = comments.find_one({"_id": new_comment_id})
theater = theaters.find_one({"_id": new_theater_id})
user = users.find_one({"_id": new_user_id})

# Printing newly added documents
pprint(movie)
print(movie['plot'])
pprint(comment['text'])
pprint(theater['location']['address']['city'])
pprint(user['email'])
