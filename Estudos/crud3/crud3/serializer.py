#É esse codigo que faz com que nosso objeto que vem da rota como json, seja retornado ao banco como objeto
from attr import fields
from flask_marshmallow import Marshmallow
 #para fazer o serializer precisamos de uma lib externa chamada marshmallow
from .model import Book


ma = Marshmallow() #não passamos app, pq iremos fazer factory, configure


def configure(app):
    ma.init_app(app)


class BookSchema(ma.Schema):#serializando a classe do sqlalchemy
    class Meta:
        model = Book
