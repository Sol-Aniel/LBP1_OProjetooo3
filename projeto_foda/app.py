from flask import Flask, render_template, redirect, url_for, request
from controllers.controller import sol_controller
app = Flask(__name__)
app.register_blueprint(sol_controller)

if __name__ == "__main__":
    app.run()