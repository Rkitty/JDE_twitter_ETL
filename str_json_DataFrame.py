#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 10:17:47 2022

@author: ro
"""


import pandas as pd
import json
#x = open('/Volumes/256xps/JDE/5_Twitter/Twitter/GuardianUS_tweets_Nov2017_Dec2017.json').read()
data = []
with open('/Volumes/256xps/JDE/5_Twitter/Twitter/GuardianUS_tweets_Nov2017_Dec2017.json') as anthony:
    for i in anthony:
        try:
            data.append(json.loads(i.rstrip(';\n')))
        except ValueError:
            print("Skipping invalid line {}".format(repr(i)))
#print(data)
#print(type(data))
df = pd.DataFrame(data)
df.to_csv('/Volumes/256xps/JDE/5_Twitter/Twitter/test_today_0620.csv')
print(df.head(1))
#print(df.columns)


'''
for i in open('/Volumes/256xps/JDE/5_Twitter/Twitter/GuardianUS_tweets_Nov2017_Dec2017.json').read():
    try:
        data.append(json.loads(i.rstrip(';\n')))
    except ValueError:
        print("Skipping invalid line {}".format(repr(i)))
'''        





'''import pandas as pd
import json
import ast
data = []

with open ('/Volumes/256xps/JDE/5_Twitter/Twitter/GuardianUS_tweets_Nov2017_Dec2017.json') as f:
    for i in f:
        try:
            data.append(json.loads(i.rstrip(';\n')))
        except ValueError:
            print("Skipping invalid line {}".format(repr(i)))
print(data)
print(type(data))
df = pd.DataFrame(data)
print(df)
print(df.columns)
    #x = f.read()
#print(x)
#print(type(x))'''







