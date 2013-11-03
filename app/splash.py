from flask import Flask, Blueprint, send_file, redirect, url_for, request


splash = Blueprint('splash', __name__)


########### Routing ###########################

@splash.route('/')
def construction():
	return send_file('static/html/index.html')

####### articles ###################################
@splash.route('/article-1/read')
def article1_read():
	return send_file('static/html/article-1-read.html')
@splash.route('/article-1/listen')
def article1_listen():
	return send_file('static/html/article-1-listen.html')

@splash.route('/article-2/read')
def article2_read():
	return send_file('static/html/article-2-read.html')
@splash.route('/article-2/listen')
def article2_listen():
	return send_file('static/html/article-2-listen.html')



@splash.route('/record-comment')
def record_comment():
	return send_file('static/html/record-comment.html')
@splash.route('/share-comment')
def share_comment():
	return send_file('static/html/share-comment.html')

