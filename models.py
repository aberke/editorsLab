# let's put all our models here for now
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from app import app


db = SQLAlchemy(app)


from datetime import datetime


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content_type = db.Column(db.Integer) # 0:text 1: audio 2: video
    title = db.Column(db.String(80))
    author = db.Column(db.String(80))
    body = db.Column(db.Text) # for text comment
    recording_url = db.Column(db.String(100))
    pub_date = db.Column(db.DateTime)



    def __init__(self, content_type, title, author, body, recording_url=None, pub_date=None):
        self.content_type = content_type
        self.title = title
        self.author = author
        self.body = body
        self.recording_url = recording_url
        if pub_date is None:
            pub_date = datetime.utcnow()
        self.pub_date = pub_date

    def __repr__(self):
        return '<Comment %r>' % self.title


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    headline = db.Column(db.String(100))
    author = db.Column(db.String(100))
    body = db.Column(db.Text)
    twilioRecordingUrl = db.Column(db.String(100))
    pub_date = db.Column(db.DateTime)

    def __init__(self, headline, author, body, pub_date=None):
        self.title = title
        self.body = body
        if pub_date is None:
            pub_date = datetime.utcnow()
        self.pub_date = pub_date
        self.category = category
