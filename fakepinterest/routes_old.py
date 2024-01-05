# criar as rotas do site
from flask import render_template
from fakepinterest import app
from flask_login import login_required
from fakepinterest.forms import FormLogin, FormCriarConta


@app.route("/", methods=["GET", "POST"])
def homepage():
	form_login = FormLogin()
	return render_template("homepage2.html", form=form_login)


@app.route("/criarconta", methods=["GET", "POST"])
def criar_conta():
	form_criarconta = FormCriarConta()
	return render_template("criarconta2.html", form=form_criarconta)


@app.route("/perfil/<usuario>")
@login_required
def perfil(usuario):
	return render_template("perfil2.html", usuario=usuario)
