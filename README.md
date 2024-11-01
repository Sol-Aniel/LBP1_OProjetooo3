# LBP1_OProjetooo3
Projeto de Laboratório de Programação

Passo-a-passo:
 - Criar a Pasta Mãe
 - Abrir o Terminal
 - cd *nome_da_pasta*
 - Lista de comando:  - python3 -m venv *nome_do_venv*-venv (criar ambiente virtual)
                      - source *nome_do_venv*-venv/bin/activate (ativar ambiente virtual)
                      - pip install flask (instalar flask)
                      - flask --version (verificar se funcionou)
 - Criar a pasta do projeto dentro da Pasta Mâe (SEPARADA DO VENV)
 - Dentro do Projeto criar o app.py
 - Dentro do Projeto criar a pasta templates (para os html's)
 - Dentro do Projeto criar a pasta static (para os css's)
 - Dentro do Projeto criar a pasta models (para os modelos, python)
 - Dentro do Projeto criar a pasta controllers (para os controllers, python)
 - Código para o app.py:
 
   from flask import Flask, render_template, redirect, url_for, request
   app = Flask(__name__)
   app.register_blueprint(*nome*_controller)
   if __name__ == "__main__":
   app.run()

- Código para os controllers:
  
  from flask import Blueprint,render_template
  
  *nome*_controller = Blueprint('qualquer coisa',__name__)

  @*nome*_controller.route('/')
  def index():
    return

- Código base para os css:

  body {
    font-family: Arial, sans-serif;
    background-color: #f2f2f2;
    margin: 0;
    padding: 0;
  }

  .container {
    max-width: 500px;
    margin: 30px auto;
    max-height: 800px;
    background-color: #fff;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 10px 5px 5px rgb(109, 60, 60);
  }

- Linha de código para chamar css no html:

  <link rel="stylesheet" href="{{ url_for('static', filename='*nome*.css') }}"
  
