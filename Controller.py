#!/usr/bin/env python

from flask import Flask
from flask import render_template
from flask import request


app = Flask(__name__)

def validate(val1, val2):
	if val1 and val2:
		return True
	return False

@app.route("/login", methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if validate(request.form['username'], request.form['password']):
			return render_template('welcome.html', name=request.form['username'])
	error = "Invalid login method"
	return render_template('hello.html', error=error)