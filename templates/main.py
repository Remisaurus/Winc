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



'''
Now write a Flask app that conforms to the specification in the following table.
Method	Path	Expected Response
GET	/	A rendering of the template index.html with the <title>: Index
GET	/about	A rendering of the template about.html with the <title>: About
Up to this point, you can test your work with pytest.
'''

if __name__ == '__main__':
   app.run(debug = True)