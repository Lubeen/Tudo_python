#Definindo a aplicação, esse é o modulo principal
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__) #Variavel especial, usada para transformar em um modulo python
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storage.db' #Caminho do banco de dados para conexao
db = SQLAlchemy(app)
migrate = Migrate(app, db)#Migrando o banco de dados, minha aplicacao e o db

manager = Manager(app) #Comando para inicializar, vai cuidar dos comandos e por padrão ja vem com ru server
manager.add_command('db', MigrateCommand)


    

