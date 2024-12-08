from SOLdao import autoresDAO
from database import db
from models import Autores

class AutoresRepository:
    
    def __init__(self) -> None:
        self.autoresDAO = autoresDAO()

    def get_autor(self, id):
        autores = self.autoresDAO.get_autor(id)
        return ([autor.toJson() for autor in autores])
    
    def get_autor_normal(self, id):
        return self.autoresDAO.get_autor(id)
    
    def get_all_autores(self):
        autores = self.autoresDAO.get_autores()
        return ([autor.toJson() for autor in autores])

    def create_autor(self, name, nacionality, birth_date):
        return self.autoresDAO.add_autor(name, nacionality, birth_date)

    def delete_autor(self, id):
        return self.autoresDAO.delete_autor(id)

    def update_autor(self, id, name, nacionality, birth_date):
        return self.autoresDAO.mod_autor(id, name, nacionality, birth_date)
