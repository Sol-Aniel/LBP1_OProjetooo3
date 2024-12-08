from models import Livros
from database import db

class livrosDAO:

    @staticmethod
    def get_livro_by_id(id):
        return Livros.query.get(id)
    
    @staticmethod
    def get_livro_by_title(title):
        return Livros.filter(Livros.title == title).all()
    
    @staticmethod
    def get_livro_by_category(category_id):
        return Livros.filter(Livros.category_id == category_id).all()
    
    @staticmethod
    def get_livro_by_author(author_id):
        return Livros.filter(Livros.author_id == author_id).all()
    
    @staticmethod
    def get_livro_by_isbn(isbn):
        return Livros.filter(Livros.isbn == isbn).all()

    @staticmethod
    def get_livros():
        return Livros.query.all()
    
    @staticmethod
    def add_livro(title, author_id, isbn, category_id, number_pages, pub_date):
        try:
            livro = Livros(title=title, author_id=author_id, isbn=isbn, category_id=category_id, number_pages=number_pages, pub_date=pub_date)
            db.session.add(livro)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return e
        
    @staticmethod
    def delete_livro(id):
        try:
            livro = livrosDAO.get_livro_by_id(id)
            db.session.delete(livro)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return e

    @staticmethod
    def mod_livro(id, title, author_id, isbn, category_id, number_pages, pub_date):
        try:
            livro = livrosDAO.get_livro_by_id(id)
            livro.title = title
            livro.author_id = author_id
            livro.isbn = isbn
            livro.category_id = category_id
            livro.number_pages = number_pages
            livro.pub_date = pub_date            
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return e