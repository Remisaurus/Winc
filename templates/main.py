from flask import Flask, render_template, redirect, url_for

__winc_id__ = "9263bbfddbeb4a0397de231a1e33240a"
__human_name__ = "templates"

app = Flask(__name__)

@app.route("/")
def index():
   return render_template('index.html')

@app.route('/home')
def reredirect():
   return redirect('http://127.0.0.1:5000')

@app.route('/about')
def about():
   return render_template('about.html')

@app.route('/content')
def content():
   return render_template('content.html')

if __name__ == '__main__':
   app.run(debug = True)