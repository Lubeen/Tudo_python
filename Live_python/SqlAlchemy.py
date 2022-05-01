'''
O conceito inicial é a junção da linguagem de programação orientada para objetos e o banco de dados
ORM(Object Relational Mapping) é uma abordagem de programação que permite ao programador escrever código de forma mais fácil e rápida,
como se fosse uma linguagem de programação orientada a objetos.

Mas pq usar SQLAlchemy?

É o mais utilizado para aplicações web, pois é mais fácil de usar e mais rápido de implementar.

from sqlalchemy.ext.declarative import declarative_engine
from sqlalchemy import Column, Integer, String

Base = declarative_base()



class User(Base):
    __tablename__ = 'users'


    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    password = Column(String(12))

#A engine é super importante para a conexão com o banco de dados, pois ela é quem vai conectar o banco de dados com o endereço 

# e  temos a sessão que é quem vai fazer a chamada da engine, podemos ter varias sessoes

'''
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()



class User(Base):
    __tablename__ = 'users'


    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    password = Column(String(12))