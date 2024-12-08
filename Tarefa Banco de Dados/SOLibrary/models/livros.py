from database import db

class Livros(db.Model):
    __tablename__ = 'livros'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False, index=True)
    author_id = db.Column(db.Integer, db.ForeignKey('autores.id'), nullable=False)
    isbn = db.Column(db.String(13), nullable=False, index=True)
    category_id = db.Column(db.Integer, db.ForeignKey('categorias.id'), nullable=False)
    number_pages = db.Column(db.Integer, nullable=False, default=0)
    pub_date = db.Column(db.Date, nullable=False)

    autores = db.relationship('Autores', back_populates='livros')
    categorias = db.relationship('Categorias', back_populates='livros')

    def __repr__(self):
        return f"<Book {self.title}>"
    
    def toJson(self):
        return {
            "id": self.id,
            "title": self.title,
            "author_id": self.author_id,
            "ISBN": self.isbn,
            "category_id": self.category_id,
            "number_pages": self.number_pages,
            "pub_date": self.pub_date,
        }