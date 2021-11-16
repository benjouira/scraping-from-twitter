import time
import tweepy
import pandas as pd

#Code d'authentification :
# you can get api twitter key from here : https://developer.twitter.com/en/apply-for-access

consumer_key= '************your consumer_key**************'
consumer_secret = '************your consumer_secret****************'
access_token_secret='***********access_token_secret***************'
access_secret='************ your access_secret ************'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_secret, access_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

try:
    api.verify_credentials()
    print("Authentication OK")
    
except:
    print("Error during authentication")
 
#   ****************************

# paste here the name of the twitter account or page
username = 'RadioMosaiqueFM' 
count = 150

try:

    tweets = tweepy.Cursor(api.user_timeline,id=username).items(count)
    tweets_list = [[tweet.created_at, tweet.id, tweet.text] for tweet in tweets]
    tweets_df = pd.DataFrame(tweets_list)

except BaseException as e:

    print('failed on_status,',str(e))

    time.sleep(3)
   
print (tweets_df)
