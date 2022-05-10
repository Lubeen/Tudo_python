from curses.ascii import BS
from flask import Blueprint, current_app, request, jsonify
from .model import Book
from .serializer import BookSchema


bp_books = Blueprint('books', __name__)

@bp_books.route('/mostrar', methods=['GET'])
def mostrar():
    bs = BookSchema(many=True)  #Ou seja irá renderizar mais de um campo pra gente na tela
    result = Book.query.all()   #Pega todos os livros
    return bs.jsonify(result), 200 
    #Retorna os livros em json



@bp_books.route('/deletar/<id>', methods=['GET'])
def deletar():
    Book.query.filter_by(Book.id == id).delete()
    current_app.db.session.commit()
    return jsonify({'message': 'Livro deletado com sucesso!'}), 200




@bp_books.route('/modificar/<id>', methods=['put'])
def modificar(id):
    bs = BookSchema()
    query = Book.query.filter_by(Book.id == id)
    query.update(request.json)#Atualizar os campos que vier pela rota para os campos que tem no banco de dados
    return bs.jsonify(query.first())

@bp_books.route('/cadastrar', methods=['post'])
def cadastrar():
    bs = BookSchema() 
    book, error = bs.load(request.json)     #vai pegar o json e transformar em um objeto na nossa classe
    current_app.db.session.add(book)     #Adiciona o objeto no banco
    current_app.db.session.commit()  #Commita o banco
    return bs.jsonify(book), 201
