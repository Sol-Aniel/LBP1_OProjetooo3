from models import Categorias
from database import db

class categoriasDAO:

    @staticmethod
    def get_categoria(id):
        return Categorias.query.get(id)

    @staticmethod
    def get_categorias():
        return Categorias.query.all()
    
    @staticmethod
    def add_categoria(name):
        try:
            categoria = Categorias(name=name)
            db.session.add(categoria)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return e
        
    @staticmethod
    def mod_categoria(id, name):
        try:
            categoria = categoriasDAO.get_categoria(id)  
            categoria.name = name
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return e
        
    @staticmethod
    def delete_categoria(id):
        try:
            autor = categoriasDAO.get_categoria(id)
            db.session.delete(autor)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return e