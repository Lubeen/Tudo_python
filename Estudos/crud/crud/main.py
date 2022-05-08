from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy
from ext.db import  SQLALCHEMY_DATABASE_URL
import json

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URL


db = SQLAlchemy(app)

class Usuario(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    telefone = db.Column(db.String(80), nullable=False)

    def to_json(self):
        return {'id': self.id, 'nome': self.nome, 'email': self.email, 'telefone': self.telefone}

#Selecionar Tudo
@app.route('/usuarios', methods=['GET'])
def seleciona_usuarios():
    usuarios_objetos = Usuario.query.all()
    usuarios_json = [usuario.to_json() for usuario in usuarios_objetos]
    return gera_response(200, 'usuarios', usuarios_json, 'ok')

#Selecionar individual
@app.route('/usuarios/<int:id>', methods=['GET'])
def seleciona_usuario(id):
    usuario_objeto = Usuario.query.filter_by(id=id).first()
    usuario_json = usuario_objeto.to_json()

    return gera_response(200, 'usuario', usuario_json, 'ok')
#Cadastrar
@app.route('/usuario', methods=['POST'])
def cadastra_usuario():
    #verifica se veio os dados
    body = request.get_json()

#Executa um try catch para verificar se ocorreu algum erro e mostrar pra gente
    try:
        usuario = Usuario(nome=body['nome'], email=body['email'], telefone=body['telefone'])
        db.session.add(usuario)
        db.session.commit()
        return gera_response(201, "usuario", usuario.to_json(), 'criado')
    
    except Exception as e:
        print(e)
        return gera_response(400, 'erro', 'erro ao criar usuario', 'erro')


#Atualizar
@app.route('/usuario/<int:id>', methods=['PUT'])
def atualiza_usuario(id):
    #pega o usuario
    usuario_objeto = Usuario.query.filter_by(id=id).first()
    #pega as modificações
    body = request.get_json()

    try:
        if ('nome' in body):
            usuario_objeto.nome = body['nome']
        if ('email' in body):
            usuario_objeto.email = body['email']
        if ('telefone' in body):
            usuario_objeto.telefone = body['telefone']

        db.session.add(usuario_objeto)
        db.session.commit()
        return gera_response(200, 'usuario', usuario_objeto.to_json(), 'atualizado')
    except Exception as e:
        print(e)
        return gera_response(400, 'erro', 'erro ao atualizar usuario', 'erro')
#Deletar
@app.route('/usuario/<int:id>', methods=['DELETE'])
def deleta_usuario(id):
    usuario_objeto = Usuario.query.filter_by(id=id).first()

    
    try:
        db.session.delete(usuario_objeto)
        db.session.commit()
        return gera_response(200, 'usuario', usuario_objeto.to_json(), 'deletado')
    except Exception as e:
        print(e)
        return gera_response(400, 'erro', 'erro ao deletar usuario', 'erro')


@app.route('/')
def hello_world():
    return 'Hello World!'


def gera_response(status, nome_do_conteudo, conteudo, mensagem=False):
    body = {}
    body[nome_do_conteudo] = conteudo

    if mensagem:
        body['mensagem'] = mensagem

    return Response(json.dumps(body), status=status, mimetype='application/json')


app.run(debug=True)