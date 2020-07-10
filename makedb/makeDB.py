#! python3

import tweepy

from tinydb import TinyDB, Query
from keysAuthentication import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def getTwitterID(name):
    user = api.get_user(name)
    return user.id_str


db = TinyDB("db/data.json")
User = Query()
getTwitterID("ChaimStanton")

# db.insert({'name': 'John', "twitter_handle": , 'twitter_id_str': 22})