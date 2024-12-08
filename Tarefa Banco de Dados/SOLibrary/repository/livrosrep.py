from SOLdao import livrosDAO, autoresDAO, categoriasDAO
from database import db
from models import Livros

class LivrosRepository:
    
    def __init__(self) -> None:
        self.livrosDao = livrosDAO()
        self.autoresDao = autoresDAO()
        self.categoriasDao = categoriasDAO()
    
    def get_all_livros(self):
        livros = self.livrosDao.get_livros()
        livrosJSON = []
        for livro in livros:
            livrosJSON.extend([livro.toJson()])
            autor = self.autoresDao.get_autor(livro.author_id)
            categoria = self.categoriasDao.get_categoria(livro.category_id)
            livrosJSON[livro.id-1]["author"] = autor.name
            livrosJSON[livro.id-1]["category"] = categoria.name
        return livrosJSON

    def get_livro_by_id(self, id):
        livros = []
        livros.extend([self.livrosDao.get_livro_by_id(id)])
        livrosJSON = []
        for livro in livros:
            livrosJSON.extend([livro.toJson()])
            autor = self.autoresDao.get_autor(livro.author_id)
            categoria = self.categoriasDao.get_categoria(livro.category_id)
            livrosJSON[livro.id-1]["author"] = autor.name
            livrosJSON[livro.id-1]["category"] = categoria.name
        return livrosJSON

    def get_livro_by_id_normal(self, id):
        return self.livrosDao.get_livro_by_id(id)

    def get_livro_by_title(self, title):
        livros =  self.livrosDao.get_livro_by_title(title)
        livrosJSON = []
        for livro in livros:
            livrosJSON.extend([livro.toJson()])
            autor = self.autoresDao.get_autor(livro.author_id)
            categoria = self.categoriasDao.get_categoria(livro.category_id)
            livrosJSON[livro.id-1]["author"] = autor.name
            livrosJSON[livro.id-1]["category"] = categoria.name
        return livrosJSON
    
    def get_livro_by_category(self, category_id):
        livros = self.livrosDao.get_livro_by_category(category_id)
        livrosJSON = []
        for livro in livros:
            livrosJSON.extend([livro.toJson()])
            autor = self.autoresDao.get_autor(livro.author_id)
            categoria = self.categoriasDao.get_categoria(livro.category_id)
            livrosJSON[livro.id-1]["author"] = autor.name
            livrosJSON[livro.id-1]["category"] = categoria.name
        return livrosJSON

    def get_livro_by_author(self, author_id):
        livros = self.livrosDao.get_livro_by_author(author_id)
        livrosJSON = []
        for livro in livros:
            livrosJSON.extend([livro.toJson()])
            autor = self.autoresDao.get_autor(livro.author_id)
            categoria = self.categoriasDao.get_categoria(livro.category_id)
            livrosJSON[livro.id-1]["author"] = autor.name
            livrosJSON[livro.id-1]["category"] = categoria.name
        return livrosJSON

    def get_livro_by_isbn(self, isbn):
        livros = self.livrosDao.get_livro_by_isbn(isbn)
        livrosJSON = []
        for livro in livros:
            livrosJSON.extend([livro.toJson()])
            autor = self.autoresDao.get_autor(livro.author_id)
            categoria = self.categoriasDao.get_categoria(livro.category_id)
            livrosJSON[livro.id-1]["author"] = autor.name
            livrosJSON[livro.id-1]["category"] = categoria.name
        return livrosJSON

    def create_livro(self, title, author_id, isbn, category_id, number_pages, pub_date):
        return self.livrosDao.add_livro(title, author_id, isbn, category_id, number_pages, pub_date)

    def delete_livro(self, id):
        return self.livrosDao.delete_livro(id)

    def update_livro(self, id, title, author_id, isbn, category_id, number_pages, pub_date):
        return self.livrosDao.mod_livro(id, title, author_id, isbn, category_id, number_pages, pub_date)