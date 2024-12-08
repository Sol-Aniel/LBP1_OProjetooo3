from SOLdao import categoriasDAO
from database import db
from models import Categorias

class CategoriasRepository:
    
    def __init__(self) -> None:
        self.categoriasDAO = categoriasDAO()

    def get_categoria(self, id):
        categorias = self.categoriasDAO.get_categoria(id)
        return ([categoria.toJson() for categoria in categorias])
        
    def get_categoria_normal(self, id):
        return self.categoriasDAO.get_categoria(id)
    
    def get_all_categorias(self):
        categorias = self.categoriasDAO.get_categorias()
        return ([categoria.toJson() for categoria in categorias])

    def create_categoria(self, name):
        return self.categoriasDAO.add_categoria(name)
    
    def update_categoria(self, id, name):
        return self.categoriasDAO.mod_categoria(id,name)

    def delete_categoria(self, id):
        return self.categoriasDAO.delete_categoria(id)
