#import mongo client
from pymongo import MongoClient

#import pprint
import pprint

#Creating instance of mongo client
client = MongoClient()

#create database
db = client.TestNoSQL

#create document
user1 = {"firstname":"David1111", "lastname":"Miller"}
user2= {"firstname":"David2222", "lastname":"Miller"}

#create collection
users = db.users

#add document to the created collection
users.insert([user1,user2])

#print added document from the collection
pprint.pprint(users.find({"firstname":"David"})[0])

