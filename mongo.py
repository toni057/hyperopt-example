# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#%%

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:1234/')
db = client['mongodbpath']
jobs = db['jobs']

#%%

l = []
for j in jobs.find({'exp_key': 'exp6'}):
    print(j)
    l.append(j)
    
    
#%%

import pandas as pd




