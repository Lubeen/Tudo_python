from os import stat
import views
import contact
from flask import Flask
import db
import admin


def create_app():
    app = Flask(__name__, template_folder='', static_folder='') #name é o nome do modulo que está sendo executado

    #configurar extensoes
    db.configure(app)

    views.configure(app)

    admin.configure(app)
    
    contact.configure(app)
    #configurar as variaveis
    app.config['SECRET KEY'] = 'oijoijoijib'
    return app
