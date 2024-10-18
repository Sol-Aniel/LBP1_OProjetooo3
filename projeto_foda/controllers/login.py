from flask import Blueprint, render_template, redirect, url_for, request, session
from models.usuarios import *

login_control = Blueprint('login',__name__)
login_control.secret_key = 'chave_screta'

@login_control.route('/')
def index():
    return render_template("login.html")

@login_control.route("/login", methods=['POST'])
def login():
    validacao = ""
    user = request.form["username"]
    key = request.form["senha"]
    if verificarUsuario(user, key)==True:
        session['username'] = request.form["username"]
        return redirect(url_for('login.dash'))
    else:
        validacao = False
        return render_template("login.html", validacao=validacao)
    
@login_control.route('/painel')
def dash():
    if 'username' in session:
        return render_template("painel.html", username = session['username'])
    else:
        return redirect(url_for('login.index'))
    
@login_control.route('/logout', methods=['POST'])
def deslogar():
    session.pop('username', None)
    return redirect(url_for('login.index'))
