# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 15:30:35 2020

@author: Melody
"""
import json

f = open("config.json", encoding='utf-8')

data = json.load(f)


'''
global data 
data = {
        "深圳":"ShenZhen",
        "Modified":"",
        }
json = json.dumps(data)

print(json)
'''