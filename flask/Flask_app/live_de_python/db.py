from http import client
from tinymongo import TinyMongoClient

#client = TinyMongoClient()

#para evitar problemas vamos usar funções ou então com classe

def get_db():
    conn = TinyMongoClient() 
    db = conn.my_database
    return db

def configure(app):#banco de dados simples
    app.db = get_db()