#!flask/bin/python
# pip install Flask
# python json_io.py

import sys

from flask import Flask, render_template, request, redirect, Response
import random, json

app = Flask(__name__)

@app.route('/')
def output():
	# serve index template
	return render_template('index.html', name='Joe')

@app.route('/receiver', methods = ['POST'])
def worker():
	# read json + reply
	data = request.get_json()
	result = ''

	for item in data:
		# loop over every row
		# result += str(item['make']) + '\n'
		make = str(item['make'])
		if(make == 'Porsche'):
			result += make + ' -- That is a good manufacturer\n'
		else:
			result += make + ' -- That is only an average manufacturer\n

	return result

if __name__ == '__main__':
	# run!
	app.run()
	#app.run("0.0.0.0", "5010")

@app.route("/output")
def output():
	return "Hello World!"
if __name__ == "__main__":
	app.run()


# <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script>
# <script type="text/javascript">
# // setup some JSON to use
# var cars = [
# 	{ "make":"Porsche", "model":"911S" },
# 	{ "make":"Mercedes-Benz", "model":"220SE" },
# 	{ "make":"Jaguar","model": "Mark VII" }
# ];

# window.onload = function() {
# 	// setup the button click
# 	document.getElementById("theButton").onclick = function() {
# 		doWork()
# 	};
# }

# function doWork() {
# 	// ajax the JSON to the server
# 	$.post("receiver", cars, function(){

# 	});
# 	// stop link reloading the page
#  event.preventDefault();
# }
# </script>
# This will send data using AJAX to Python:<br /><br />
# <a href="" id="theButton">Click Me</a>


