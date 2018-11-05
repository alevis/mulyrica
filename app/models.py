import hashlib 
from datetime import datetime
from app import db

class Record(db.Model):
	__tablename__ = 'record'
	id = db.Column(db.Integer, primary_key=True)
	artist = db.Column(db.String(64),index=True,unique=True)
	timestamp = db.Column(db.String(64),index=True,unique=True)
	songs = db.relationship('Songs',backref='artist',lazy='dynamic')
	
	def __init__(self,artist):
		self.artist = artist
	def __repr__(self):
		return '<Artist: %s>' % self.artist

class Songs(db.Mode):
	''' A template for storing songs.
		param dictionary: positive, negative, neutral, compound
	'''
	id = db.Column(db.Integer,primary_key=True)
	# Analysis information
	positive = db.Column(db.Float,index=True,unique=True)
	negative = db.Column(db.Float,index=True,unique=True)
	compound = db.Column(db.Float,index=True,unique=True)
	neutral = db.Column(db.Float,index=True,unique=True)
	# Song information
	album = db.Column(db.String(20),index=True,unique=True)
	date = db.Column(db.String(10),index=True,unique=True)	# The date of release
	lyrics = db.Column(db.String(1000),index=True,unique=True) # Song lyrics
	songs = db.Column(db.String(20),db.ForeignKey('Record.songs')) # Link back to the record
	def __init__(self,positive,negative,compound,neutral,album,date,lyrics):
		self.positive = positive
		self.negative = negative
		self.compound = compound
		self.neutral = neutral
		self.lyrics = lyrics
		self.album = album
		self.date = date
	def __repr__(self):
		return '<Positive=%s, Negative=%s, Neutral=%s,\
				Compound=%s, lyrics=%s, album=%s\
				date=%s>' % (self.positive,self.negative,self.neutral,self.compound,\
							 self.neutral, self.lyrics, self.album, self.date)