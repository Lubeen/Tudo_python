#Definindo a aplicação, esse é o modulo principal
from flask import Flask

app = Flask(__name__) #Variavel especial, usada para transformar em um modulo python

from app.controllers import default

    

