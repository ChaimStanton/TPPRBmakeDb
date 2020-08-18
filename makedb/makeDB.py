#! python3

import tweepy

from tinydb import TinyDB, Query
from keysAuthentication import *
from time import sleep

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def getTwitterID(name):
    try:
        user = api.get_user(name)
        return user.id_str
    except tweepy.error.TweepError:
        print("User" + name + "not found")
        return 1


class MP():
    def __init__(self, handleWat):
        self.handleWat = handleWat
        self.id_str = getTwitterID(handleWat)

while True:
    print("""
    1 - Make the database of MP's from a csv
    2 - Enter a handle get the ID
    3 - Make keys authentication database
    9 - Exit
    """)
    choice = input("What is your selection: ")
    if choice == "1":
        politicalParty = input("Enter the political party: ")
        db = TinyDB("db/" + politicalParty + ".json")
        print("""
Save your file in the input_data as a csv
save it in the input_data folder
        """)
        fileName = input("Input the name: ")

        try: 
            with open("input_data/"+ fileName, "r") as data:
                dataList = data.read().splitlines()
        except FileNotFoundError:
            print("File NOT found")
            sleep(1.5)
            continue # restarts the while loop

        print(dataList)

        MPs = []
        for MPstrHandle in dataList:
            MPs.append(MP(MPstrHandle))

        for MP in MPs:
            db.insert({'Handle': MP.handleWat, "id_str": MP.id_str})

    elif choice == "2":
        try:
            name = input("Enter the username: ")
            print(getTwitterID(name))
        except tweepy.error.TweepError:
            print("Invalid username")

    elif choice == "3":
        print("Entering keys authentication creation part")
        politicalParty = input("Enter the political party: ")

        db = TinyDB("db/" + politicalParty + "KEYS.json")

        consumer_key = input("Enter the consumer_key : ")
        consumer_secret = input("Enter the consumer_secret : ")
        access_token = input("Enter the access_token : ")
        access_token_secret = input("Enter the access_token_secret : ")

        print("Creating database now .... ")
        sleep(1)
        
        db.insert({'consumer_key': consumer_key})
        db.insert({"consumer_secret": consumer_secret})
        db.insert({"access_token" : access_token})
        db.insert({"access_token_secret" : access_token_secret})
        
        print("Done")

    elif choice == "9":
        print("Thank you goodbye")
        quit()
    else:
        print("Invalid choice")