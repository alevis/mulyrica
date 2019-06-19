from os import environ as envkey
import tweepy
from tweepy import OAuthHandler
import load_env

music_key = envkey.get('music_key')
# Twitter access tokens and secret keys
consumer_key = envkey.get('consumer_key')
consumer_secret = envkey.get('consumer_secret')
access_token = envkey.get('access_token')
access_secret = envkey.get('access_secret')

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

def test_keys():
	print 'music key: ', music_key
	print 'consumer key: ', consumer_key
	print 'consumer secret: ', consumer_secret
	print 'access token ', access_token
	print 'access secret: ', access_secret	

# test_keys()

def get_timeline():
	for status in tweepy.Cursor(api.home_timeline).items(10):
		print status.text

def tagsearch():
	search_tag = '#BetterDays'
	for status in tweepy.Cursor(api.search, q = search_tag).items(10):
		print status.text

tagsearch()
