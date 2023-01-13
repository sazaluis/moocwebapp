# -*- coding: iso-8859-15 -*-

import sys

from flask import Flask, render_template

app = Flask(__name__)
from flask import request

# CODIGO PARA RENDER DE ERRORES
def process_error(message, next_page):
    """

    :param message:
    :param next_page:
    :return:
    """
    return render_template("error.html", error_message=message, next=next_page)
@app.route('/')
def index():
    """
    It process the '/' url.
    :return: basic HTML
    """

    return app.send_static_file('index.html')

@app.route('/home')
def home():

    return app.send_static_file('home.html')

""" OLD LOGIN APP ROUTE
@app.route('/login')
def login():

    return app.send_static_file('login.html')
"""
@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    It process '/login' url (form for login into the system)
    :return: firstly it will render the page for filling out the login data. Afterwards it will process these data.
    """
    if request.method == 'POST':
        missing = []
        fields = ['email', 'passwd', 'login_submit']
        for field in fields:
            value = request.form.get(field, None)
            if value is None or value == '':
                missing.append(field)
        if missing:
            return render_template('missingFields.html', inputs=missing, next=url_for("login"))
        return load_user(request.form['email'], request.form['passwd'])
    return app.send_static_file('login.html')

@app.route('/signup')
def signup():

    return app.send_static_file('signup.html')

@app.route('/processSignup', methods=['GET', 'POST'])
def processSignup():
    missing = []
    fields = ['nickname', 'email', 'passwd','confirm', 'signup_submit']
    for field in fields:
        value = request.form.get(field, None)
        if value is None:
            missing.append(field)
    if missing:
        return "Warning: Some fields are missing"

    return '<!DOCTYPE html> ' \
           '<html lang="es">' \
           '<head>' \
           '<link href="static/css/socnet-style.css" rel="stylesheet" type="text/css"/>' \
           '<title> Home - SocNet </title>' \
           '</head>' \
           '<body> <div id ="container">' \
		   '<a href="/"> SocNet </a> | <a href="home"> Home </a> | <a href="login"> Log In </a> | <a href="signup"> Sign Up </a>' \
           '<h1>Data from Form: Sign Up</h1>' \
           '<form><label>Nickame: ' + request.form['nickname'] + \
	       '</label><br><label>email: ' + request.form['email'] + \
	       '</label><br><label>passwd: ' + request.form['passwd'] + \
	       '</label><br><label>confirm: ' + request.form['confirm'] + \
           '</label></form></div></body>' \
           '</html>'

@app.route('/agent')
def agent():
 user_agent = request.headers.get('User-Agent')
 return '<p>Your browser is %s</p>' % user_agent

# start the server with the 'run()' method
if __name__ == '__main__':
    if sys.platform == 'darwin':  # different port if running on MacOsX
        app.run(debug=True, port=8080)
    else:
        app.run(debug=True, port=80)
