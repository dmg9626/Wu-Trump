#!/usr/bin/python

import os
import sys
import tweepy
import HTMLParser

# read API keys from files
f_ckey = open("API/consumer_key")
consumer_key = f_ckey.read().strip()

f_csecret = open("API/consumer_secret")
consumer_secret = f_csecret.read().strip()

f_atkey = open("API/access_token_key")
access_token_key = f_atkey.read().strip()

f_atsecret = open("API/access_token_secret")
access_token_secret = f_atsecret.read().strip()

# OAuth
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)
filename="Trump/trump.txt"

f = open(filename,"w+")

i = 0
limit = 1000

# fetch tweets
for status in tweepy.Cursor(api.user_timeline, count=limit, screen_name='@realDonaldTrump', tweet_mode='extended').items():
    
    # skip retweets
    if hasattr(status, 'retweeted_status'):
        continue
    
    # get full text and parse symbols correctly (ex. &amp -> &)
    full_text = status._json['full_text']
    tweet = HTMLParser.HTMLParser().unescape(full_text)

    # write tweet text to file (make sure to encode as UTF-8 to avoid encode error when writing)
    f.write(tweet.encode('utf-8') + "\n")
    
    # stop if reached limit
    i += 1
    if i >= limit:
        break

print "wrote",i,"tweets to",filename
f.close()
