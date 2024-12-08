from database import db

class Autores(db.Model):
    __tablename__ = 'autores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True, index=True)
    nacionality = db.Column(db.String(80))
    birth_date = db.Column(db.Date, nullable=False)

    livros = db.relationship('Livros', back_populates='autores', lazy=True)

    def __repr__(self):
        return f"<Author {self.name}>"
    
    def toJson(self):
        return {
            "id": self.id,
            "name": self.name,
            "nacionality": self.nacionality,
            "birth_date": self.birth_date,
        }