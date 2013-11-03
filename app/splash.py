from flask import Flask, Blueprint, send_file, redirect, url_for, request


splash = Blueprint('splash', __name__)


########### Routing ###########################

@splash.route('/')
def construction():
	return send_file('static/html/index.html')

@splash.route('/article/1')
def article():
	return send_file('static/html/article-1.html')

@splash.route('/article/audio')
def test():
	return send_file('static/html/article-audio.html')
