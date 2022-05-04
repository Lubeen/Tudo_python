from sqlalchemy import ForeignKey
from app import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    name = db.Column(db.String(80), nullable=False)

    def __init__(self, username, email, password, name):#Quando a classe for inicializada, o construtor será chamado
        self.username = username
        self.email = email
        self.password = password
        self.name = name

    def __repr__(self):
        return '<User %r>' % self.username # aqui vai mostrar por vez
    

class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)


    user = db.relationship('User', foreign_keys=[user_id])#está relacionando todas as informaçoes do usuario na tabela

    def __init__(self, title, content, user_id):
        self.title = title
        self.content = content
        self.user_id = user_id

    def __repr__(self):
        return '<Post %r>' % self.id 


class Follow(db.Model):
    __tablename__ = "follow"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    follower_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    user = db.relationship('User', foreign_keys=[user_id])
    follower = db.relationship('User', foreign_keys=[follower_id])
