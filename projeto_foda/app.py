from flask import Flask, render_template, redirect, url_for, request, flash, abort
from controllers.controller import sol_controller
from controllers.login import login_control

app = Flask(__name__)
app.secret_key = 'chave_screta'
app.register_blueprint(sol_controller)
app.register_blueprint(login_control)

if __name__ == "__main__":
    app.run()
