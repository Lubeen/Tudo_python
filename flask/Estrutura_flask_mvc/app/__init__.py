#Definindo a aplicação, esse é o modulo principal
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) #Variavel especial, usada para transformar em um modulo python
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storage.db' #Caminho do banco de dados para conexao
db = SQLAlchemy(app)

from app.controllers import default

    

