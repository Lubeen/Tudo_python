#views = são as funções que vão ser executadas quando for chamada uma rota
# from app import app #nao importamos o app aqui
from flask import jsonify, render_template

def configure(app):#Quando for executado a unica coisa que vai acontecer é criar uma definicao da funcao configure, ele nao vai ser executado só definido

    @app.route('/')
    def index():
        return '<h1>Essa é a primeira rota</h1>'

    @app.route('/rota2')
    def raiz():
        return '<h1>Essa é a segunda rota</h1>'

    @app.route('/pessoa/<string:nome>/<string:cidade>')
    def pessoas(nome, cidade):
        #return '<h1>Nome: {}<br>Cidade: {}</h1>'.format(nome, cidade)
        return jsonify({'nome': nome, 'cidade': cidade})

    @app.route('/langs')
    def langs():
        languages = ['Python', 'Java', 'C#', 'C++']
        return render_template(
            'index.html', 
            title="Melhores linguagens",
            linguagens=languages
        )