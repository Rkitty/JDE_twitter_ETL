#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 17:06:28 2022

@author: rockylee
"""

import pandas as pd

#關鍵字fitter 2個或以上 or 關係｜
columns = ['ID','Twitter','created_at','like_count','retweet_count']
df = pd.read_csv('/Users/rockylee/Desktop/Junior Data Engineer progrmar/ALL_Project/Twitter/JoeBiden_twitter2.csv',index_col=0)
print(type(df))
df = df[df['Twitter'].str.contains('COVID|COVID-19|COVID 19|covid|\
                                    covid-19|covid 19|Vaccination|VACCINATION｜\
                                        coronavirus',case=False)]
#rint(df.iloc[:,0])
print(df)
#df2.to_csv('JoeBiden_twitter_fittering.csv')
'''for i in df.iloc[:,0]:
    print(i)'''


'''
print('_______________________________________________________________')
#僅顯示某列列表
print(df[['ID','created_at']])
#僅顯示單列
print(df['ID'])
#數據切片loc & iloc
print(df.loc[:2,'ID':'created_at'])
print(df.iloc[0:2,[0,4]])
print(df.iloc[0:2,0:2])
print('_______________________________________________________________')
'''












