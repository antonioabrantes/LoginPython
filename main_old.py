# This is a sample Python script.
# escolha
# http://127.0.0.1:5000
# pip freeze > requirements.txt

# https://blp.hashtagtreinamentos.com/python/minicurso/criacao-sites-python

# Aula 1: Visão geral
# https://www.youtube.com/watch?v=yjgRxATKeqQ

# Aula 2: Flask
# https://www.youtube.com/watch?v=kJShv2RuOY0&t=142s

# Aula 3: Criar projeto
# https://www.youtube.com/watch?v=U8wSOVez7A8
# abrir terminal e digite pip install flask
# verifique pip list
# execute main.py
# veja http://127.0.0.1:5000

# Aula 4: Templates
# https://www.youtube.com/watch?v=sEfZluCY6BM

# Aula 5: Rotas dinâmicas
# https://www.youtube.com/watch?v=yPuHaMxOhjM

# Aula 6 - Conectando as páginas do nosso site [Curso de Criação de Sites com Python]
# https://www.youtube.com/watch?v=QY36rOvO3qM

# Aula 7 - Criando templates base html [Curso de Criação de Sites com Python]
# https://www.youtube.com/watch?v=cXfD3cZlvv0

# Aula 8 - Criando um banco de dados
# https://www.youtube.com/watch?v=60qY34XmSKU
# pip install flask-sqlalchemy
# instale https://sqlitebrowser.org/dl/

# Aula 9 - Implementar sistema de login e segurança [Curso de Criação de Sites com Python]
# https://www.youtube.com/watch?v=RNv1ErRNWu4
# pip install flask-login flask-bcrypt

# Aula 10 - Criar formulários de login e de criar conta [Curso de Criação de Sites com Python]
# https://www.youtube.com/watch?v=sFI-tZVPLnQ
# pip install flask-wtf
# pip install email_validator

# Aula 11 - Implementar o formulário de login na homepage e de criar conta [Criação de Sites Python]
# https://www.youtube.com/watch?v=tmOf43Iy3YY

# Aula 12 - Implementar funcionalidades de Login e Criar Conta [Curso de Criação de Sites com Python]
# https://www.youtube.com/watch?v=zIO1n9mU9x4

# Aula 13 - Logout do Usuário e Atualizando o Perfil do Usuário [Curso de Criação de Sites com Python]
# https://www.youtube.com/watch?v=evDMbEg-tIw

# Aula 14 - Criar o gerenciamento de imagens [Curso de Criação de Sites com Python]
# https://www.youtube.com/watch?v=GlNtnxFE1K0

# Aula 15 - Criando a funcionalidade de postar uma foto [Curso de Criação de Sites com Python]
# https://www.youtube.com/watch?v=2D7kMVQ_U-g

# Aula 16 - Criar feed do pinterest [Curso de Criação de Sites com Python]
# https://www.youtube.com/watch?v=8A6plRDdjaU

# Aula 17 - Ajustando o Layout com um template [Curso de Criação de Sites com Python]
# https://www.youtube.com/watch?v=I55wR-zTNdY

# Aula 18 - Implementanto Layout para todas as páginas [Curso de Criação de Sites com Python]
# https://www.youtube.com/watch?v=TGk9TOU8mkk

# Aula 19 - Finalização e Continuação [Curso de Criação de Sites com Python]
# https://www.youtube.com/watch?v=-Q9fA8-zMuE

# template
# https://startbootstrap.com/previews/freelancer
# webchat rasa
# https://rasa.com/docs/rasa/connectors/your-own-website/
# https://github.com/botfront/rasa-webchat
# https://medium.com/desenvolvendo-com-paixao/ngrok-do-localhost-para-o-mundo-5445ad08419

from fakepinterest import app


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
