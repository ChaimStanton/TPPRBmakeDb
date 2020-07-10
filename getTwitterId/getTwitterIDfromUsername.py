#! python3

from keysAuthentication import *

import tweepy

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def getID(name):
    user = api.get_user(name)
    return user.id_str

if __name__ == "__main__":
    
    print(getID("ChaimStanton"))

    try:
        txtFile = open("usernames.txt", "r")
        for name in txtFile:
            print(name.rstrip("\n"))
            # print(name[:-2])
            user = api.get_user(name)
            print(user.id_str)
    except FileNotFoundError:
        print("File not found")