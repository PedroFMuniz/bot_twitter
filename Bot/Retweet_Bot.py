import tweepy
import time
from config import TOKEN, CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET

client = tweepy.Client(TOKEN, CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)

tweets = client.search_recent_tweets(query='Termo', max_results=100)

tweets = client.get_users_tweets(id='Id_Usuario', max_results=100)

for tweet in tweets.data:
    client.retweet(tweet.id)
    time.sleep(5)