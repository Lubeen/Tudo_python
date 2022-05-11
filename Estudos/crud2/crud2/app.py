from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Pessoa(db.Model):
    __tablename__ = 'clientes'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80))
    idade = db.Column(db.Integer)
    cpf = db.Column(db.String(14))

    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

    
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cadastrar', methods=['GET'])
def cadastrar_usuario():
    return render_template('cadastro.html')

@app.route('/cadastro', methods=['GET' ,'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form.get['nome']
        idade = request.form.get['idade']
        cpf = request.form.get['cpf']

        if nome and idade and cpf:
            p = Pessoa(nome, idade, cpf)
            db.session.add(p)
            db.session.commit()
    return redirect(url_for('index'))

@app.route('/listar', methods=['GET'])
def listar_usuarios():
    pessoa = Pessoa.query.all()
    if request.method == 'POST':
        nome = request.form.get['nome']
        idade = request.form.get['idade']

        if nome and idade:
            pessoa.nome = nome
            pessoa.idade = idade

            db.session.commit()
        return redirect('lista.html')
    return render_template('lista.html')


@app.route('/excluir/<int:id>', methods=['DELETE'])
def excluir_usuario(id):
    pessoa = Pessoa.query.get(id).first()
    db.session.delete(pessoa)
    db.session.commit()
    return redirect(url_for('listar_usuarios'))

@app.route('/editar/<int:id>', methods=['GET','POST'])
def editar_usuario(id):
    pessoa = Pessoa.query.get(id).first()
    return render_template('editar.html', pessoa=pessoa)



if __name__ == '__main__':
    app.run(debug=True)
