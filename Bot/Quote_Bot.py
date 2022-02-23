import tweepy
import time
from config import TOKEN, CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET


client = tweepy.Client(TOKEN, CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)

client.create_tweet(text='Mensagem', quote_tweet_id='Id_Tweet')