#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 17:31:25 2022

@author: rockylee
"""

import psycopg2
import tweepy
import pandas as pd

#api 4 key
api_key = 'uF0DOC3pQoNjgNnQOK1Wi088v'
api_key_secret = '7lOS2UZ5F7XuFQielKpwEMf16Jij6mlZU6FZaGVR9uaNEbPZ8w'
access_token = '2682699414-Si4SU72snug3AgKaAlMTXA9eoDAUoYUW4rAdvPs'
access_token_secret = 'tb2NbDAvMUybh1xhBH9J8sr4pJw370lPyQESdUKf29dEi'
#V2
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAPhZbQEAAAAAWlO7emrosFXKGy9zBT4CXmbjTDk%3DDPiSasUXGwEewJvUZCFJ97SOUexP2taTEg4ZvN9D2NWwy8lMQo'

#login
auth = tweepy.OAuth1UserHandler(api_key, api_key_secret)
auth.set_access_token(access_token , access_token_secret)
api = tweepy.API(auth)

cursor = tweepy.Cursor(api.user_timeline, id="Rocky_Lee_3636", 
                       tweet_mode='extended').items(3)

conn = psycopg2.connect(database = 'friday',user = 'postgres', password = '1234', host = '127.0.0.1',port='5432')
cursor = conn.cursor()
sql = 'select version()'
cursor.execute(sql)
data = cursor.fetchone()
print('database version : %s ' % data)
conn.commit()
conn.close()
#連結
conn = psycopg2.connect(database='friday',user='postgres',password='1234',host='127.0.0.1',port='5432')
cursor = conn.cursor()
sql = 'select version()'
cursor.execute(sql)
data = cursor.fetchone()
print('database version : %s ' % data)
conn.commit()
conn.close()



