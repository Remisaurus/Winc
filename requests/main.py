__winc_id__ = "cc1b724762854e85a8defa04287f708b"
__human_name__ = "requests"

'''
For this exercise, you will need to read Flask's documentation:

Flask -- Quickstart
Create a Flask application that can be run as follows:

export FLASK_APP=main.py
flask run
It should then serve content according to the specifications in this table:

method	path	expected response content
GET	/	<p>Home, sweet home.</p>
GET	/greet	<h1>Hello, world!</h1>
GET	/greet/<example_name>	<h1>Hello, example_name!</h1>
You can test your implementation with the pytest, which runs the test in the test_main.py file we supplied with wincpy start.
'''

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<p>Home, sweet home.</p>'

@app.route('/greet/')
def greet():
    return b'<h1>Hello, world!</h1>'

@app.route('/greet/<someone>')
def greetings(someone):
    string = f"<h1>Hello, {someone}!</h1>"
    return string
