from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def configure(app):#Agora para linkarmos isso ao banco precisamos fazer a config aqui
    db.init_app(app)
    app.db = db #só para ter algo para chamar

class Book(db.Model):#Representação da tabela
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    livro = db.Column(db.String(80), nullable=False)
    autor = db.Column(db.String(80), nullable=False)


 
