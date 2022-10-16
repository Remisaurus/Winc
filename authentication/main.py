import os

from flask import Flask, redirect, render_template, request, session, url_for
from helpers import get_users, hash_password

__winc_id__ = "8fd255f5fe5e40dcb1995184eaa26116"
__human_name__ = "authentication"

app = Flask(__name__)

app.secret_key = os.urandom(16)


@app.route("/home/")
def redirect_index():
    return redirect(url_for("index"))

@app.route("/")
def index():
    return render_template("index.html", title="Index")

@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route("/lon")
def lon():
    return render_template("lon.html", title="League of Nations")

@app.route('/password/<name>', methods=["GET", "POST"])
def password(name):
    if name not in get_users():
        return redirect(url_for('login'))
    if request.method == 'POST':
            password = request.form['password']
            if hash_password(password) == get_users()[name]:
                session[name] = name
                return redirect(url_for('dashboard', name=name))
            else:
                return render_template('password.html', title='login2error', name=name)      
    else:
            return render_template('password.html', title='login2', name=name)
        
@app.route('/dashboard/<name>')
def dashboard(name):
    if name in session:
        return render_template('dashboard.html', name=name)
    else:
        return 'Access denied. try logging in again from step 1.'
    
@app.route("/login/", methods=["GET", "POST"])
def login():  
    if request.method == 'POST':
            user = request.form['username']
            if user in get_users():
                return redirect(url_for('password', name=user))
            else:
                return render_template('login.html', title='loginerror')
    else:
        return render_template('login.html', title='login')


@app.route("/logout/<name>", methods=["GET", "POST"])
def logout(name):
    session.pop(name)
    return render_template('logout.html')

if __name__ == '__main__':
   app.run(debug = True)
