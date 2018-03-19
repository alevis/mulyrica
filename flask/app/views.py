from PyLyrics import *
from nltk import tokenize
from nltk.sentiment.util import *
from nltk.corpus import subjectivity
from nltk.classify import NaiveBayesClassifier
from nltk.sentiment.vader import SentimentIntensityAnalyzer

from flask_wtf import FlaskForm
from flask import render_template, url_for
from wtforms import StringField, SubmitField
from app import app

music_key = '9c510f91c9b12de4a037d3896d89a3'

class MyForm(FlaskForm):
	artist = StringField(u'artist')
	song = StringField(u'song')
	submit = SubmitField(u'submit')

@app.route('/',methods=['GET','POST'])
@app.route('/index',methods=['GET','POST'])
def index():
	results=[]
	analysis = {'neu':0.0,'pos':0.0,'neg':0.0,'compound':0.0}	
	score=dict()
	length = 0
	form = MyForm()	
	if form.is_submitted():
		lyrics = PyLyrics.getLyrics(form.artist.data,form.song.data)
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
	return render_template('index.html',title='Mulyrica',form=form)
