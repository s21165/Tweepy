from textblob import TextBlob
import tweepy
import configparser
import pandas as pd
import datetime

from textblob import TextBlob
import sys
import tweepy
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import nltk
import pycountry
import re
import string
from wordcloud import WordCloud, STOPWORDS
from PIL import Image

from langdetect import detect
from nltk.stem import SnowballStemmer

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()
from sklearn.feature_extraction.text import CountVectorizer

tweet_list = []
neutral_list = []
negative_list = []
positive_list = []
positive = 0
negative = 0
neutral = 0

# read configs
config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

# authentication
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)





startDate = datetime.datetime(2017, 12, 1)
endDate =   datetime.datetime(2017, 12, 2, 0, 0, 0)




api = tweepy.API(auth)
polarity = 0
noOfTweet = 1
KEYWORDS = "bitcoin OR python"
tweets = tweepy.Cursor(api.search_tweets, q=KEYWORDS,
                    lang="en",

                   result_type="recent").items(noOfTweet)
vader_analyzer = SentimentIntensityAnalyzer()
tweets2=[]

today = datetime.date.today()
print(today)




for tweet in tweets:
    print(tweet.text, '\n')

    print('test')
    print(tweet.created_at)
    print(endDate)


    print(startDate.day)
    print (tweet.geo, "to jest geo?")
    print(tweet.coordinates)

    # Twitter ID of London
    id = "457b4814b4240d87"


    # fetching the location
    location = api.geo_id(id)

    # printing the information
    print("Place Type : " + location.place_type)
    print("Name : " + location.name)
    print("Full Name : " + location.full_name)
    print("Country : " + location.country)

    if tweet.created_at.year < endDate.year and tweet.created_at.year > startDate.year:

        tweets2.append(tweet)

    tweet_list.append(tweet.text)
    analysis = TextBlob(tweet.text)
    score = SentimentIntensityAnalyzer().polarity_scores(tweet.text)
    neg = score['neg']
    neu = score['neu']
    pos = score['pos']
    comp = score['compound']
    polarity += analysis.sentiment.polarity
    if neg > pos:
        negative_list.append(tweet.text)
        negative += 1
    elif pos > neg:
        positive_list.append(tweet.text)
        positive += 1

    elif pos == neg:
        neutral_list.append(tweet.text)
        neutral += 1

print('neg score= ', neg);
print('neu score= ', neu);
print('pos score= ', pos);

tweets2 = []





   ## if tweet.created_at < endDate and tweet.created_at > startDate:
      ##  tweets2.append(tweet)



s1 = "Britain’s trade will be much worse if it doesn’t have a good trade deal."

vs = analyzer.polarity_scores(s1)

"""
keyword = 'test'
noOfTweet = 10
##tweets = tweepy.Cursor(api.search_tweets, q=keyword).items(noOfTweet)
positive = 0
negative = 0
neutral = 0
polarity = 0
tweet_list = []
neutral_list = []
negative_list = []
positive_list = []
    
    for tweet in tweets:
    # print(tweet.text)
    tweet_list.append(tweet.text)
    analysis = TextBlob(tweet.text)
    score = SentimentIntensityAnalyzer().polarity_scores(tweet.text)

    neg = score[‘neg’]
    neu = score[‘neu’]
    pos = score[‘pos’]
    comp = score[‘compound’]
    polarity += analysis.sentiment.polarity

    if neg > pos:
        negative_list.append(tweet.text)
    negative += 1
elif pos > neg:
positive_list.append(tweet.text)
positive += 1

elif pos == neg:
neutral_list.append(tweet.text)
neutral += 1
positive = percentage(positive, noOfTweet)
negative = percentage(negative, noOfTweet)
neutral = percentage(neutral, noOfTweet)
polarity = percentage(polarity, noOfTweet)
positive = format(positive, ‘.1f’)
negative = format(negative, ‘.1f’)
neutral = format(neutral, ‘.1f’)





api = tweepy.API(auth)
KEYWORDS = "bitcoin OR python"
public_tweets = api.search_tweets(KEYWORDS)
print(public_tweets[0].text)

# create dataframe
columns = ['Time', 'User', 'Tweet']
data = []
for tweet in public_tweets:
    data.append([tweet.created_at, tweet.user.screen_name, tweet.text])

df = pd.DataFrame(data, columns=columns)

df.to_csv('tweets.csv')

"""
