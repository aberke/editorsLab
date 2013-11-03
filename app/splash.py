from flask import Flask, Blueprint, send_file, redirect, url_for, request


splash = Blueprint('splash', __name__)


########### Routing ###########################

@splash.route('/')
def construction():
	return send_file('static/html/index.html')

@splash.route('/article-read.html')
def article_read():
	return send_file('static/html/article-1.html')

@splash.route('/article-listen')
def article_listen():
	return send_file('static/html/article-listen.html')

@splash.route('/record-comment')
def record_comment():
	return send_file('static/html/record-comment.html')
