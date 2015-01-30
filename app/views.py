from app import app
from flask import render_template, redirect, url_for, request

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/shorten_url', methods=['GET', 'POST'])
def shortenURL():
	newUrl = request.form['url']
	return render_template('shorten_url.html', newUrl=newUrl)