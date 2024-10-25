from flask import Blueprint, Response, render_template, redirect, url_for, request, session, flash, abort, make_response
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
        flash('Login efetuado', 'success')
        session['username'] = request.form["username"]
        return redirect(url_for('login.dash'))
    else:
        flash('Usuário não encontrado ou senha incorreta', 'danger')
        return render_template("login.html")
    
@login_control.route('/painel')
def dash():
    if verificarAdmin(session['username'])==True:
        return render_template("painel.html", username = session['username'])
    else:
        return render_template("compras.html", username = session['username'], carrinho = session['carrinho'])

@login_control.route('/painel', methods=["POST", "GET"])
def carrinho():
    if verificarAdmin(session['username'])==True:
        return render_template("painel.html", username = session['username'])
    else:
        frutas = request.form["frutas"]
        quant =request.form["quantidade"]
        r = make_response("Cookie has been set!")
        q = make_response("Cookie has been set!")
        r.set_cookie(frutas, frutas, max_age=60*60)
        q.set_cookie((frutas + 'q'), quant, max_age=60*60)
        adicionarCarrinho(request.cookies.get(frutas), request.cookies.get(frutas + 'q'))
        return render_template("compras.html", username = session['username'], carrinho = carrinho)
 

@login_control.route('/logout', methods=['POST'])
def deslogar():
    session.pop('username', None)
    session.pop('carrinho', None)
    return redirect(url_for('login.index'))
