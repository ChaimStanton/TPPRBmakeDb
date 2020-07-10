#! python3

import tweepy

from tinydb import TinyDB, Query

db = TinyDB("db/data.json")
User = Query()
db.insert({'name': 'John', 'twitter_id_str': 22})