from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'For now, this flask app does not do much more than getting updated for the assignment.\n \
        Changes can be made easily here, and after pushed it gets tested and then uploaded to the VPS.'

@app.route('/<anything>/')
def anything(anything):
    return f'Yes keep trying.. (you tried: {anything}..)'

@app.route('/<anything>/<more>/')
def end(anything, more):
    return f"Now you've reached the end, congratulations. (you tried: {anything}/{more}).."

def gotta_test_some(x, y):
    return x + y