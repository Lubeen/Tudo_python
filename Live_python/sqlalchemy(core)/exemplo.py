from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey,delete, update

#sqlalchemy com core

engine = create_engine('sqlite:///test.db', echo= True)
#Criar a tabela
MetaData = MetaData(bind=engine) #metadados para a engine
user_table = Table('user', MetaData,
                    Column('id', Integer, primary_key=True),
                    Column('name', String(50)),
                    Column('fullname', String(50)),
                    Column('password', String(12)))

MetaData.create_all() #para criar a tabela
 
'-----------------------------------------------------------------------------------'
#Para inserir dados na tabela
conn = engine.connect() #para conectar a engine 

ins = user_table.insert()#para inserir valores

new_user = ins.values = {'name': 'jose', 'fullname': 'jose bezerra', 'password': '123'}

conn.execute(new_user) #para executar a inserção

conn.execute(user_table.inset(), [
    {'name': 'jose', 'fullname': 'jose bezerra', 'password': '123'},
    {'name': 'jose', 'fullname': 'jose bezerra', 'password': '123'},
    {'name': 'jose', 'fullname': 'jose bezerra', 'password': '123'},
    {'name': 'jose', 'fullname': 'jose bezerra', 'password': '123'},
])

#para atualizar os valores da tabela

u = update(user_table).where(user_table.c.name == 'jose')

u = u.values(name='Luben')

result = conn.execute(u)#para executar a atualização

print(result.rowcount)#mostra quantas linhas foram alteradas

#para deletar dados da tabela
d = delete(user_table).where(user_table.c.name == 'jose')

result = conn.execute(d) #para executar

print(result.rowcount) #mostra quantas linhas foram alteradas
