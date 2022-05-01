from sqlalchemy import create_engine, Column, Integer, String, ForeignKey #a primeira coisa a fazer e vamos dizer com quem conectar
from sqlalchemy.ext.declarative import declarative_base #database
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('sqlite:///test.db', echo=True)#3 barras para criar no diretorio atual e echo para ele me contar
Session = sessionmaker(bind=engine)#Diz para mim onde esta a engine que eu quero conectar
session = Session()

Base = declarative_base()

class Produto(Base):
    __tablename__ = 'produtos'#Nome da tabela no banco de dados

    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    preco = Column(Integer)
    pessoa_id = Column(Integer, ForeignKey('pessoas.id'))
    pessoa = relationship("Pessoa")


class Pessoa(Base):
    __tablename__ = 'pessoas'#Nome da tabela no banco de dados

    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    idade = Column(Integer)
    produtos = relationship("Produto", backref="pessoa")

Base.metadata.create_all(engine)#cria a tabela

p1 = Pessoa(nome='Joao', idade=20)
p2 = Pessoa(nome='Maria', idade=25)
p3 = Pessoa(nome='Jose', idade=30)
p4 = Pessoa(nome='Pedro', idade=35)
p5 = Pessoa(nome='Ana', idade=40)

session.add_all([p1, p2, p3, p4])#adiciona todos os objetos na tabela
session.commit()#salva no banco de dados

session.add(p5)#adiciona um objeto na tabela
session.flush()#Apaga o ultimo comando adicionado
from pprint import pprint
pprint(session.query(Pessoa).all())
