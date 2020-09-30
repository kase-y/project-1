import random

import tweepy
from authorization_tokens import *
from corpus.templates import *
from markov_chain import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

possible_tweets = {
    "template_news_story": str_template(),
    "markov news story": breaking_news(),
    "markov_tech_quote": tech_markov()
}

message = random.choice(list(possible_tweets.values()))
api.update_status(message)

print("Done.")
print("POSTED: " + message)
