#!/usr/bin/env python
# coding: utf-8

# # Project Assessmen: How to ETL twitter information.
#                                                                                           Create 2022-5-1 
#                                                                                           Author Rocky_Lee
#     

# ##    1. About the Program
#         1.Overall Goal
#            -   Specify a Twitter user and crawl all of that user's tweets.
#            -   Data cleansing, filtering out worthless information from your Twitter feed
#            -   Specify keywords to filter twitter content
#            -   Design the database and save the relevant data
# 
#         2.How to use the program?
#            -   set some specify keywords on python
#            -   use Python capture data
#            -   use PgSQL command or Python load the data and analysis
#            -   Edit ER-D
#            -   SQLit3 run for python, PgSQL show for data visualization 

# ##    2.About the Program tools: Install and Setup
#         - python: https://www.python.org
#         +- configparser:pip install configparser
#         +- tweepy:pip install tweepy
#         - SQLite3:https://www.sqlite.org/index.html
#         +- sqlalchemy:pip install sqlalchemy
#         +- pandas:pip install pandas
#         
#         

# ##    3.Input the variable : Global
#         set 1: Open and Run the Python Program.
#         set 2: In terminal define the necessary parameters.

# In[ ]:


print('Define the necessary parmeters: ')
user = (input('  Please enter your target\'s Twitter ID: '))
print('\n')
print('If you want to get the maximum, just click "Enter/Return" only: ')
page = (input('  please enter how many recode is your want to get: '))


# 
# ## 4.Call  and Run key.ini File
#     Please make sure you have the developer account key
#     More detailed: https://developer.twitter.com/en

# In[2]:


import configparser

#read configs
'''
In this INI file, all keys for logging in to the API are saved.
The beta version will use the developer key.
If you need to define keys, please contact your developer or Twitter.
    More detailed: https://developer.twitter.com/en
'''
config = configparser.ConfigParser()
config.read('config.ini')
api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']
access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']


# ## 5.Call tweepy and login Twitter API
#     About more API detailed:https://developer.twitter.com/en/search-results?limit=10&offset=0&q=api&searchPath=%2Fcontent%2Fdeveloper-twitter%2Fen&sort=relevance
#     - Login V1.0 Free without limit
#     - Login V2: Limited use and capped free
#     
#     About how to choose the tools from tweepy, Please read the Tweepy.DOC
#     https://docs.tweepy.org/en/stable/
#     
#     Since our goal and for exam i will choose user_timeline(): For Example
#     

# In[3]:


import tweepy

'''
    when you want to call the V1 API, just call the 'api' 
'''

#login V1 and set the api:
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
#login V2 and set the client:
client = tweepy.Client(consumer_key = api_key,
                       consumer_secret = api_key_secret,
                       access_token = access_token,
                       access_token_secret = access_token_secret)


# ## 6.ETL --> E

# In[7]:


import json
#import tweepy  --part.5 We imported the python library.
'''
Call the tweepy.api.user_timeline() get the user infomation from twitter.
    line 10 --> pages(x), text x you can input any int, for get a number pages infomation.
    For all about info, we use append save in data(class list)
    For each data type where key and velue is class json 
    maybe we need to show about json format, so import Json first
'''

def timeline(user):
    data = []
    for user_tweet in tweepy.Cursor(api.user_timeline,
                                    screen_name = user,
                                    tweet_mode = 'extended').pages():
        for i_json in user_tweet:
            data.append(i_json._json)
    return data
timeline(user)


# In[5]:


#get the follower.


# ## 7.ETL --> T
#     Obviously, the data is not readable. 
#     So... we need to translation
#     Usually, we use pandas to translation, of course, cleansing data is part of that.
#     Translation consists of two parts, one is data cleaning, the other is keyword filtering.

# In[8]:


import pandas as pd

# define two empty list, columns sava the table title, value save the data value. 

value = []
def data_key():
    columns = []
    t_data_0 = timeline(user)
    for key,value in t_data_0[0].items():
        columns.append(key)
    return columns


print(value)


# In[6]:


# usually two-dimension can easy to read.
columns = data_key()
print(columns)
df = pd.DataFrame(timeline(user),columns=columns)#.set_index('created_at')
print(df.head())


# In[9]:


#自動檢索刪除，發現有整列 null，無可讀性，清除

df = df.dropna(axis=1,how='all')
print(df.head())
print(df.shape)


# In[10]:


# 手動檢索刪除 發現有大量False，id有兩列，無可讀性或冗余， 清除
# 經過檢查，侷限使用usertime（） 如果更替為其他檢索工具，需要再校對代碼

#missing_values 是經過手動檢索需要刪除都列類別。（為多列刪除）
missing_values = ['id_str','truncated','is_quote_status','favorited','retweeted']

#指定的單列刪除
#del df['id_str']

#執行對missing_values 列表的指定刪除列
df1 = df.drop(missing_values,axis = 1, inplace = False)

#對刪除列後結果進行輸出
#print(df)
                                                                                    #print(df.iloc[:,6])

#df1 為全局定義，保留可讀性數據
#df2 為全局定義，保留指定數據
#經過過濾後的結果，只保留了以下資料： df2
df2 =df1.drop(['display_text_range','entities','source','user','lang'],axis = 1, inplace = False)
'''
    - 創建推文的時間 created_at
    - 推文所屬的識別號 id
    - 推文的全文內容 full_text 
    - 推文的讚好量 retweet_count
    - 推文的轉發量 favorite_count
    '''
print(df2.head())


# In[11]:


#df3 將保存以關鍵字過濾的有關信息
#print(df)


df3 = df['full_text'].str.contains('COVID|COVID-19|COVID 19|                                    covid|covid-19|covid 19|                                        Vaccination|VACCINATION｜                                            coronavirus', case = False)
print(df3)
'''for i in df3.index:
    print(df3.loc[i])'''


# ## 7.ETL --> L

# In[12]:


import sqlalchemy
#設計數據庫保存數據
# call the local Datebase
db_location = '/Users/rockylee/Downloads/assessment_SQLite_3/pj_db_twitter.db'
def sql_command(q):
    engine = sqlalchemy.create_engine("sqlite:///{}".format(db_location))
    df2 = pd.read_sql(q , engine)
    print(df2)
    print('\n')
'''while(True):
    table_name = str(input('叫你系度打Command： '))
    sql_command(table_name)'''


# In[ ]:


import time
#定義主資料表關機字 data lake～～
main_user = 'main_' + str(user)

#創建主數據表
create_df = '''CREATE TABLE IF NOT EXISTS "{}" (created_at datetime,id int,twitter text,like_count int,retweet_count int,fittering bool);'''.format(main_user)
#執行表格創建
try:
    sql_command(create_df)
except:
    print('Create Table {} is successful.'.format(main_user))

#插入主數據表數據
'''.replace('\'',' ')
maybe values[2] need to add this command
'''
count_successful = 0
for i in df2.index:
    time.sleep(1)
    sql_command_insert = """ insert or ignore into "{}" values ('{}','{}','{}','{}','{}','{}');"""    .format(main_user,            str(df2.loc[i].values[0]),            str(df2.loc[i].values[1]),            str(df2.loc[i].values[2]),            str(df2.loc[i].values[3]),            str(df2.loc[i].values[4]),            df3.loc[i])
    count_successful += 1
    #sql_command(sql_command_insert)
    try:
        sql_command(sql_command_insert)
    except:
        print('successful adding: ' + str(count_successful) + ' record.')


# In[ ]:





# In[ ]:





# In[ ]:




