import tweepy
from textblob import TextBlob

consumer_key = "Pjww70CZ9wjxOWTEOuikm3kF7"
consumer_secret = "8jN3hT8hgfgPCM6wc7KvpUwPE6UXSPQNJkmXXj2YMyzsZ4vnmJ"

access_token = "963435850053881856-vGI22MtP5ldgRE9ZLSpQAFjeYNWNNQs"
access_token_secret = "PPsvQRsCzWMOiVCB2YEUdeOhEURRlFC0Xzz1Pawl5Qds5"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search("frontend")

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)