from models import Autores
from database import db

class autoresDAO:

    @staticmethod
    def get_autor(id):
        return Autores.query.get(id)

    @staticmethod
    def get_autores():
        return Autores.query.all()
    
    @staticmethod
    def add_autor(name, nacionality, birth_date):
        try:
            autor = Autores(name=name, nacionality=nacionality, birth_date=birth_date)
            db.session.add(autor)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return e
        
    @staticmethod
    def delete_autor(id):
        try:
            autor = autoresDAO.get_autor(id)
            db.session.delete(autor)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return e

    @staticmethod
    def mod_autor(id, name, nacionality, birth_date):
        try:
            autor = autoresDAO.get_autor(id)  
            autor.name = name
            autor.nacionality = nacionality
            autor.birth_date = birth_date
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return e