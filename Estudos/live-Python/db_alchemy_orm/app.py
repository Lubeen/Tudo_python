from sqlalchemy import sqlalchemy
from sqlalchemy import Column, Integer, String

#Conectando ao banco de dados, engine = ferramenta de conexao com o banco de dados
engine = sqlalchemy.create_engine('sqlite:///enterprise.db', echo=True)

#Declarando o mapeamento entre o objeto python e o banco de dados, ou seja a partir do declarative base, 
# ja podemos criar nosso objeto com ligação ao banco de dados
from sqlalchemy import declarative_base
Base = declarative_base()

class User(Base):#Utilizamos o base para criar nossa classe
    __tablename__ = 'users'#Obrigatorio

    id = Column(Integer, primary_key=True)#Obrigatorio
    name = Column(String(50))
    fullname = Column(String(50))
    password = Column(String(12))

    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password
        

    def __repr__(self):#Só para visualizar mais bonito
        return "<User(name='%s', fullname='%s', password='%s')>" % (self.name, self.fullname, self.password)

#Criar a tabela no banco de dados
Base.metadata.create_all(engine)

#Criar instancias da classe
user = User(name='ed', fullname='Ed Jones', password='edspassword')

#Para fazer a adição primeiro precisamos da sessao 
#Criar uma sessao
from sqlalchemy import sessionmaker 

Session = sessionmaker(bind=engine)
session = Session()

#Adicionar Objetos ao banco de dados(INSERT)
session.add(user)#Ficou salvo na memoria do python
session.commit()#Foi salvo no banco de dados
session.add_all([
    User(name='wendy', fullname='Wendy Williams', password='foobar'),
    ])#Adicionar varios objetos

#Consultar objetos(SELECT)
query_user = session.query(User).filter_by(name='enzo').first()#Query=consulta, aqui filtrou em user pelo nome enzo
query_user.name
#Todos os usuarios
for instance in session.query(user).order_by(User.id):#aqui nao filtrou pegou todos os usuarios
    print(instance.name, instance.fullname)
 
#Atualizar objetos(UPDATE)
user.fullname = 'Enzo Bezerra'
session.dirty #para ver se tem algo que foi alterado
session.new #para ver se tem algo que foi adicionado
session.commit()#Salvar no banco de dados

#Deletar objetos(DELETE)
user = session.query(User).filter_by(name='ed').first()
session.delete(user)#Deleta o objeto na memoria
session.commit()#Salvar no banco de dados