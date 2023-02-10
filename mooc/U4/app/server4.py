# -*- coding: iso-8859-15 -*-

import sys

from flask import Flask, render_template

app = Flask(__name__)
from flask import request,url_for,redirect
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


def load_user(email, passwd):
    """
    It loads data for the given user (identified by email) from the data directory.
    It looks for a file whose name matches the user email
    :param email: user id
    :param passwd: password to check in order to validate the user
    :return: content of the home page (app basic page) if user exists and password is correct
    """
    SITE_ROOT = os.path.abspath(os.path.dirname("server4.py"))
    file_path = os.path.join(SITE_ROOT, "data/", email)
    file_path = file_path+".json"
    if not os.path.isfile(file_path):
        return process_error("User not found / No existe un usuario con ese nombre", url_for("login"))
    with open(file_path, 'r') as f:
        data = json.load(f)
    if data['password'] != passwd:
        return process_error("Incorrect password / la clave no es correcta", url_for("login"))
    session['user_name'] = data['user_name']
    session['messages'] = data['messages']
    session['password'] = passwd
    session['email'] = email
    session['friends'] = data['friends']
    return redirect(url_for("home"))

def save_current_user():
    datos = {
        "user_name": session["user_name"],
        "password": session['password'],
        "messages": session['messages'], # lista de tuplas (time_stamp, mensaje)
        "email": session['email'],
        "friends": session['friends']
    }
    file_path = os.path.join(SITE_ROOT, "data/", session['email'])
    with open(file_path, 'w') as f:
        json.dump(datos, f)

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

    directory = os.path.join(SITE_ROOT, "data")
    if not os.path.exists(directory):
        os.makedirs(directory)
    file_path = os.path.join(SITE_ROOT, "data/", email)
    if os.path.isfile(file_path):
        return process_error("The email is already used, you must select a different email / Ya existe un usuario con ese nombre", url_for("signup"))
    if passwd != passwd_confirmation:
        return process_error("Your password and confirmation password do not match / Las claves no coinciden", url_for("signup"))
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

@app.route('/showmessages', methods=['GET', 'POST'])
def showmessages():
    datos={}
    if request.method == 'POST':

        if session:
            friends = session['friends']
            for email in friends:
                frienddata = readuserdata()
                ret_message = frienddata.get("messages")

                datos[frienddata['user_name']] = {}
                datos[frienddata['user_name']]['messages'] = frienddata['messages']

        else:
            return process_error("Tienes que loguearte primero", url_for("login"))

        return render_template('returnuserdata.html', inputs=datos, next=readuserdata)
    return app.send_static_file('readuserdata.html')
def readuserdata():
        datos={}
        email = request.form.get('email', None) + ".json"
        if email is None or email == '':
            missing.append(email)
        SITE_ROOT = os.path.dirname(__file__)
        file_path = os.path.join(SITE_ROOT, "data/", email)
        if not os.path.isfile(file_path):
            return process_error("User not found / No existe un usuario con ese nombre", "readuserfriends")
        with open(file_path, 'r') as f:
            datos= json.load(f)
        return datos

def get_friends_messages_with_authors():
    """buscará los amigos del usuario actual (pista: deberían estar guardados en la sesión) y para cada uno de ellos cargará
    el fichero correspondiente donde se guardan sus mensajes. La función debe retornar una lista de tuplas, cada una
    representando un mensaje de la forma (user, time_stamp, message).

    Recomendación: para facilitar el desarrollo de un código más fácil de entender y mantener, te recomiendo que uses 2
     funciones: la primera que cargue la lista de amigos desde la sesión y, para cada uno de ellos, la segunda función
      cargue el fichero correspondiente.
    """



    get_messages_from_users()

def load_session_user_friends():
    session['friends']

def get_messages_from_users():
    a = a + 1

# start the server with the 'run()' method
if __name__ == '__main__':
    if sys.platform == 'darwin':  # different port if running on MacOsX
        app.run(debug=True, port=8080)
    else:
        app.run(debug=True, port=80)
