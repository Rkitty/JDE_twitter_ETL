import tweepy
import pandas as pd

consumer_key = 'uF0DOC3pQoNjgNnQOK1Wi088v'
consumer_secret = '7lOS2UZ5F7XuFQielKpwEMf16Jij6mlZU6FZaGVR9uaNEbPZ8w'
access_token = '2682699414-Si4SU72snug3AgKaAlMTXA9eoDAUoYUW4rAdvPs'
access_token_secret = 'tb2NbDAvMUybh1xhBH9J8sr4pJw370lPyQESdUKf29dEi'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# the screen_name of the targeted user 
screen_name = "JoeBiden"


data=[]
columns=  ['id','name','created_at','location']
# printing the latest 300 followers of the user
for follower in tweepy.Cursor(api.get_followers, screen_name = "JoeBiden").items(1):
    #print('Name - ' + str(follower.screen_name))
    #print('User ID - ' + str(follower.id))
    #print('Joined at - ' + str(follower.created_at))
    #print('Location - ' + str(follower.location))
    print(follower)
    abc = follower
    data.append([follower.id,
                 follower.screen_name,
                 follower.created_at,
                 follower.location])


                 
a = tweepy.Cursor(api.get_followers, screen_name = "JoeBiden").items(1)
print(type(a))        
                 
'''
df = pd.DataFrame(data,columns = columns)
df.to_csv('mavis_follower_1.csv',index=False)
print(df)'''
