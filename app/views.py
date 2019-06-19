from os import environ as envkey
import re
from PyLyrics import *
from nltk import tokenize
from nltk.sentiment.util import *
from nltk.corpus import subjectivity
from nltk.classify import NaiveBayesClassifier
from nltk.sentiment.vader import SentimentIntensityAnalyzer

import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

from flask_wtf import FlaskForm
from flask import render_template, url_for
from wtforms import StringField, SubmitField
from app import app

music_key = envkey.get('music_key')
# Twitter access tokens and secret keys
consumer_key = envkey.get('consumer_key')
consumer_secret = envkey.get('consumer_secret')
access_token = envkey.get('access_token')
access_secret = envkey.get('access_secret')

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

class MyForm(FlaskForm):
	artist = StringField(u'artist')
	song = StringField(u'song')
	submit = SubmitField(u'submit')

class MyListener(StreamListener):
	def on_data(self, data):
		try:
			with open('python.json', 'a') as f:
				f.write(data)
				return True
		except BaseException as e:
			print "Error on_data: %s " % str(e)
		return True
	
	def on_error(self, status):
		print status
		return True

#twitter_stream = Stream(auth, MyListener())
#twitter_stream.filter(track=['#python'])
				

def test_keys():
	print 'music key: ', music_key
	print 'consumer key: ', consumer_key
	print 'consumer secret: ', consumer_secret
	print 'access token ', access_token
	print 'access secret: ', access_secret	

# test_keys()

def get_timeline():
	timeline = []
	for status in tweepy.Cursor(api.home_timeline).items(10):
		timeline.append(status.text)
	return timeline

def tag_search(hashtag):
	hashtag = re.sub(r"[^A-Za-z]+", '', hashtag)
	hashtag = '#' + hashtag.lower()
	results = []
	print hashtag
	for tweet in tweepy.Cursor(api.search, q=hashtag).items(10):
		results.append(tweet.text)
	print results
	return results

@app.errorhandler(404)
def page_not_found(e):
    return render_template('not_found.html'), 404

@app.route('/',methods=['GET','POST'])
@app.route('/index',methods=['GET','POST'])
def index():
	results=[]
	analysis = {'neu':0.0,'pos':0.0,'neg':0.0,'compound':0.0}
	score=dict()
	length = 0
	form = MyForm()
        artist = ''
        song = ''
	if form.is_submitted():
                song = str(form.song.data)
                artist = str(form.artist.data)
		result = PyLyrics.getLyrics(artist, song)
		album = result[0]
		lyrics = result[1]
		if lyrics is None:
			return render_template('not_found.html',title='Mulyrica',form=form)

		lyrics = lyrics.split("\n")
		sid = SentimentIntensityAnalyzer()
		for line in lyrics:
			if line and line.strip() and not(line=="(x2)"):
				score = sid.polarity_scores(line)
				analysis['neu'] += score['neu']
				analysis['pos'] += score['pos']
				analysis['neg'] += score['neg']
				analysis['compound'] += score['compound']
				results.append(score)
		length = len(results)
		analysis['neu'] = analysis['neu']/length
		analysis['neg'] = analysis['neg']/length
		analysis['pos'] = analysis['pos']/length
		analysis['compound'] = analysis['compound']/length
		return render_template('index.html',title='Mulyrica',\
			results=zip(lyrics,results),analysis=analysis,form=form, tweets=tag_search(album))
	return render_template('index.html',title='Mulyrica',form=form)

@app.route('/index2', methods=['GET','POST'])
def index2():
	form = MyForm()
	results=[]
	analysis = {'neu':0.0,'pos':0.0,'neg':0.0,'compound':0.0}
	score=dict()
	length = 0
	form = MyForm()
	if form.is_submitted():
		result = PyLyrics.getLyrics(form.artist.data,form.song.data)
		album = result[0]
		lyrics = result[1]
		lyrics = lyrics.split("\n")
		sid = SentimentIntensityAnalyzer()
		for line in lyrics:
			if line and line.strip() and not(line=="(x2)"):
				score = sid.polarity_scores(line)
				analysis['neu'] += score['neu']
				analysis['pos'] += score['pos']
				analysis['neg'] += score['neg']
				analysis['compound'] += score['compound']
				results.append(score)
		length = len(results)
		analysis['neu'] = analysis['neu']/length
		analysis['neg'] = analysis['neg']/length
		analysis['pos'] = analysis['pos']/length
		analysis['compound'] = analysis['compound']/length
		return render_template('index.html',title='Mulyrica',\
			results=zip(lyrics,results),analysis=analysis,form=form)
	return render_template('index2.html',title='Mulyrica',form=form)
