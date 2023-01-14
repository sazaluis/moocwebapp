# -*- coding: iso-8859-15 -*-

import sys

from flask import Flask, render_template

app = Flask(__name__)
from flask import request,url_for
from flask import Flask, session
from datetime import datetime
import json
import os
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

# CODIGO PARA RENDER DE ERRORES
def process_error(message, next_page):
    """

    :param message:
    :param next_page:
    :return:
    """

    return render_template("error.html", error_message=message, next=url_for(next_page))

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
    if request.method == 'POST':
        missing = []
        fields = ['nickname', 'email', 'passwd','confirm', 'signup_submit']
        for field in fields:
          value = request.form.get(field, None)
          if value is None:
              missing.append(field)
        if missing:
            return "Warning: Some fields are missing"
        create_user_file(request.form['nickname'],request.form['email'],request.form['passwd'],request.form['confirm'])
    return app.send_static_file('signup.html')
@app.route('/agent')
def agent():
 user_agent = request.headers.get('User-Agent')
 return '<p>Your browser is %s</p>' % user_agent

@app.route('/procesarNombre',methods=['POST'])
def procesa_nombre():
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    session['nombre'] = nombre
    session['apellido'] = apellido
    return 'Hola ' + nombre + ' ' + apellido

def create_user_file(name, email, passwd, passwd_confirmation):
    """
    It creates the file (in the /data directory) for storing user data. The file name will match the user email.
    If the file already exists, it returns an error.
    If the password does not match the confirmation, it returns an error.
    :param name: Name or nickname of the user
    :param email: user email, which will be later used for retrieving data
    :param passwd: password for future logins
    :param passwd_confirmation: confirmation, must match the password
    :return: if no error is found, it sends the user to the home page
    """
    SITE_ROOT = os.path.dirname(__file__)
    directory = os.path.join(SITE_ROOT, "data")
    if not os.path.exists(directory):
        os.makedirs(directory)
    file_path = os.path.join(SITE_ROOT, "data/", email)
    if os.path.isfile(file_path):
        return process_error("The email is already used, you must select a different email / Ya existe un usuario con ese nombre", "signup")
        return load_user(request.form['nickname'], request.form['email'], request.form['passwd'], request.form['confirm'])
    if passwd != passwd_confirmation:
        return process_error("Your password and confirmation password do not match / Las claves no coinciden", "signup")
        return load_user(request.form['nickname'], request.form['email'], request.form['passwd'], request.form['confirm'])
    datos = {
        "user_name": name,
        "password": passwd,
        "messages": [],
        "friends": []
    }
    with open(file_path, 'w') as f:
        json.dump(datos, f)
    session['user_name'] = name
    session['password'] = passwd
    session['messages'] = []
    session['friends'] = []
    session['email'] = email
    return redirect(url_for("home"))




# start the server with the 'run()' method
if __name__ == '__main__':
    if sys.platform == 'darwin':  # different port if running on MacOsX
        app.run(debug=True, port=8080)
    else:
        app.run(debug=True, port=80)
