import tweepy
import os
import datetime
import flask
import requests
import os
import sys

app = flask.Flask(__name__)

consumer_key = os.environ["API_KEY"]
consumer_secret = os.environ["API_KEY_SECRET"]
access_token = os.environ["ACCESS_TOKEN"]
access_token_secret = os.environ["ACCESS_TOKEN_SECRET"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

account = "taylorswift13"

@app.route('/')
def index():

    user = api.get_user(account)
    screen_name = user.screen_name
    user_name = user.name
    description = user.description
    
    user_tweets = api.user_timeline(account)
    end_date = datetime.datetime.now() - datetime.timedelta(days=30)
    
    tweet_list = []
    tweet_time = []
    
    # get all tweets in the last 30 days
    for tweet in user_tweets:
      
        if tweet.created_at < end_date: 
            break
        
        tweet_list.append(tweet.text)
        tweet_time.append(tweet.created_at)
       
    return flask.render_template(
        "index.html",
        screen_name = screen_name,
        user_name = user_name,
        description = description,
        tweet_list = tweet_list,
        tweet_time = tweet_time,
        list_len = len(tweet_list),
        time_len = len(tweet_time))
    
app.run(
    port = int(os.getenv("PORT", 8080)),   
    host = os.getenv("IP", "0.0.0.0")
)