from flask import Flask,jsonify, render_template, redirect, url_for, request, flash, abort
from flask_sqlalchemy import SQLAlchemy
from database import db, init_db
from models import Livros
from controllers import *

app = Flask(__name__)
init_db(app)

app.register_blueprint(library)

if __name__ == "__main__":
    app.run()
