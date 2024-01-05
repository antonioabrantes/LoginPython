# criar as rotas do nosso site (os links)
from flask import render_template, url_for, redirect
from fakepinterest2 import app

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/perfil/<id_usuario>")
def perfil(id_usuario):
    return render_template("perfil.html")

