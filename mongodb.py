# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 13:47:42 2020

@author: Melody
"""
import json

import pymongo

from pymongo import MongoClient

#============Read & Load data from config.json===================#
f = open("config.json", encoding='utf-8')

data = json.load(f)
#================================================================#

client = pymongo.MongoClient("mongodb+srv://m220student:1993827jhd@mflix.s1mof.mongodb.net/<dbname>?retryWrites=true&w=majority")

db = client.gettingStarted

people1 = db.people2 #collection

people1.insert_one(data)




