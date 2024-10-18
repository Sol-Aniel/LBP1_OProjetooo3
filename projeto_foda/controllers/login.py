from flask import Blueprint, render_template, redirect, url_for, request, session, flash, abort
from models.usuarios import *

login_control = Blueprint('login',__name__)
login_control.secret_key = 'chave_screta'

@login_control.before_request
def verifica():
    lista = ['login.index', "login.login"]
    if 'username' not in session and request.endpoint not in lista:
        return redirect(url_for('login.index'))

@login_control.route('/')
def index():
    return render_template("login.html")

@login_control.route("/login", methods=['POST'])
def login():
    user = request.form["username"]
    key = request.form["senha"]
    if verificarUsuario(user, key)==True:
        flash('Login efetuado', 'alert-success')
        session['username'] = request.form["username"]
        return redirect(url_for('login.dash'))
    else:
        flash('Usuário não encontrado ou senha incorreta', 'alert-error')
        return render_template("login.html")
    
@login_control.route('/painel')
def dash():
    return render_template("painel.html", username = session['username'])
    
@login_control.route('/logout', methods=['POST'])
def deslogar():
    session.pop('username', None)
    return redirect(url_for('login.index'))
