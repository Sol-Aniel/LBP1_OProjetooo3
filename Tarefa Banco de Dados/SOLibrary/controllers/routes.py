from flask import Flask,jsonify, render_template, Blueprint, redirect, url_for, request, flash, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from database import db, init_db
from models import *
from SOLdao import *
from repository import *

library = Blueprint('sol',__name__)
livros_repository = LivrosRepository()
autores_repository = AutoresRepository()
categorias_repository = CategoriasRepository()

@library.route ("/")
def index():
    mensagem=''
    return render_template('index.html', mensagem=mensagem)

@library.route ("/sua-lista")
def lista():
    livros = livros_repository.get_all_livros()
    autores = autores_repository.get_all_autores()
    categorias = categorias_repository.get_all_categorias()
    return render_template('lista.html', livros=livros, autores=autores, categorias=categorias)

@library.route ('/add', methods=['POST','GET'])
def add():
    if request.method == 'POST':
        tipo = request.form['form_type']        
        if tipo == 'livro':
            titulo = request.form['title']
            autor_id = request.form['author']
            isbn = request.form['isbn']
            category_id = request.form['category']
            numero_paginas = request.form['number_pages']
            pub_data = request.form['pub_date']
            pub_data = datetime.strptime(pub_data, '%Y-%m-%d').date()
            livros_repository.create_livro(titulo, autor_id, isbn, category_id, numero_paginas, pub_data)
            mensagem = 'Livro Adicionado !'
            return redirect(url_for('sol.index', mensagem=mensagem))
        elif tipo == 'autor':
            nome = request.form['name']
            nacionalidade = request.form['nacionality']
            data_nasc = request.form['birth_date']
            data_nasc = datetime.strptime(data_nasc, '%Y-%m-%d').date()
            autores_repository.create_autor(nome, nacionalidade, data_nasc)
            mensagem = 'Autor Adicionado'
            return redirect(url_for('sol.index', mensagem=mensagem))
        elif tipo == 'categoria':
            nome = request.form['name']
            categorias_repository.create_categoria(nome)
            mensagem = 'Categoria Adicionado !'
            return redirect(url_for('sol.index', mensagem=mensagem))
    else:
        autores = autores_repository.get_all_autores()
        categorias = categorias_repository.get_all_categorias()
        return render_template('add.html', autores=autores, categorias=categorias)
    
@library.route('/edit')
def ledit():
    livros = livros_repository.get_all_livros()
    autores = autores_repository.get_all_autores()
    categorias = categorias_repository.get_all_categorias()
    return render_template('edit.html', livros=livros, autores=autores, categorias=categorias)

@library.route('/delete/<path:tipo>/<int:id>', methods=['POST'])
def delete(tipo, id):
    if tipo == 'livro':
        livros_repository.delete_livro(id)
        mensagem = 'Livro Deletado'
        return redirect(url_for('sol.index', mensagem=mensagem))
    elif tipo == 'autor':
        autores_repository.delete_autor(id)
        mensagem = autores_repository.delete_autor(id)
        return redirect(url_for('sol.index', mensagem=mensagem))
    elif tipo == 'categoria':
        categorias_repository.delete_categoria(id)
        mensagem = 'Categoria Deletada'
        return redirect(url_for('sol.index', mensagem=mensagem))
    
@library.route('/editar/<path:tipo>/<int:id>', methods=["POST", 'GET'])
def edit(tipo, id):
    if request.method == 'POST':       
        if tipo == 'livro':
            titulo = request.form['title']
            autor_id = request.form['author']
            isbn = request.form['isbn']
            category_id = request.form['category']
            numero_paginas = request.form['number_pages']
            pub_data = request.form['pub_date']
            pub_data = datetime.strptime(pub_data, '%Y-%m-%d').date()
            livros_repository.update_livro(id, titulo, autor_id, isbn, category_id, numero_paginas, pub_data)
            mensagem = 'Livro Atualizado'
            return redirect(url_for('sol.index', mensagem=mensagem))
        elif tipo == 'autor':
            nome = request.form['name']
            nacionalidade = request.form['nacionality']
            data_nasc = request.form['birth_date']
            data_nasc = datetime.strptime(data_nasc, '%Y-%m-%d').date()
            autores_repository.update_autor(id, nome, nacionalidade, data_nasc)
            mensagem = 'Autor Atualizado'
            return redirect(url_for('sol.index', mensagem=mensagem))
        elif tipo == 'categoria':
            nome = request.form['name']
            categorias_repository.update_categoria(id, nome)
            mensagem = 'Categoria Atualizada'
            return redirect(url_for('sol.index', mensagem=mensagem))
    else:
        autores = autores_repository.get_all_autores()
        categorias = categorias_repository.get_all_categorias()
        if tipo == 'livro':
            livro = livros_repository.get_livro_by_id_normal(id)
            title = livro.title
            author = autores_repository.get_autor_normal(livro.id)
            author = author.name
            isbn = livro.isbn
            category = categorias_repository.get_categoria_normal(livro.id)
            category = category.name
            number_pages = livro.number_pages
            pub_date = livro.pub_date
            return render_template('editar.html', id=id, title=title, author=author,isbn=isbn, category=category, number_pages=number_pages, pub_date=pub_date, autores=autores, categorias=categorias, tipo=tipo)
        elif tipo == 'autor':
            autor = autores_repository.get_autor_normal(id)
            name = autor.name
            nacionality = autor.nacionality
            birth_date = autor.birth_date
            return render_template('editar.html', id=id, name=name, nacionality=nacionality, birth_date=birth_date, autores=autores, categorias=categorias, tipo=tipo)
        elif tipo == 'categoria':
            categoria = categorias_repository.get_categoria_normal(id)
            name = categoria.name
            return render_template('editar.html', id=id, name=name, autores=autores, categorias=categorias, tipo=tipo)
