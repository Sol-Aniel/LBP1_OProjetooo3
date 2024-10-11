from flask import Blueprint,render_template
from models.model import Estrela, estrelas

sol_controller = Blueprint('sol',__name__)

@sol_controller.route('/')
def index():
    return render_template("hestia.html", estrelas=estrelas)
