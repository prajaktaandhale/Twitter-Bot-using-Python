import tweepy
import time 

#creds
auth = tweepy.OAuthHandler('F65nYoxP5rSF2GCvhYmyGTgf9' , 'ur8QEgt7J2ugicpmSCLauprXMNOVOzIfAQMOAXnbhflvb2aH1W')
auth.set_access_token('1309177113652662272-4rrOUk9Pxn9KccGPnATO2IUypgT8tr', '1K3NjvrLHuMYeR4xfpp2CpLENsgqrPugZ4WvTtI6ZAyO5' )

api = tweepy.API(auth)
user = api.me()
#print("user creds: ", user)

#api.update_status("Hello, this is a test with bukola")

#for following in tweepy.Cursor(api.friends).items():
 #   print(following.name)

#randomly likes a tweet based on keywords 
# search = 'UniversityofHouston'
# num_tweet = 2

# for tweet in tweepy.Cursor(api.search, search).items(num_tweet):
#     try:
#         print("tweet liked")
#         tweet.favorite()
#         time.sleep(1)
    
#     except tweepy.TweepyError as e:
#         print(e.reason)

#     except StopIteration:
#         break

tweet_account = api.user_timeline(screen_name = "jay_hopee")
for tweet in tweet_account:
    if tweet.text[0:2] != "RT":
        tweet.favorite()
        print("liked my own tweet")
        