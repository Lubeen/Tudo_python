from flask import Flask
from flask_migrate import Migrate #migração pede que configure o banco antes
from .model import configure as config_db
from .serializer import configure as config_ma


def create_app():
    app = Flask(__name__)   

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/crud3.db'#ONde o banco vai ser criado
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    config_db(app)#Chamando a função que inicializa o banco
    config_ma(app)#Chamando a função que inicializa o marshmallow
    
    Migrate(app, app.db)#Migração
    
    #flask db init para criar a pasta migrations e flask db migrate para criar a migração
    from .books import bp_books as bp
    app.register_blueprint(bp)
    #Registrando a blueprint no app

    return app
