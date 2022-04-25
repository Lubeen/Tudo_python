from flask_admin import Admin

from flask_admin.contrib.pymongo import ModelView #apartir daqui posso criar views

from wtforms import fields, form #criando um formulario pronto do wtforms


class MessageForm(form.Form):
    name = fields.StringField('Nome')
    message = fields.TextAreaField('Mensagem')

class MessageView(ModelView):
    form = MessageForm
    column_list = ('name',)#precisa colocar um virgula no final para o python saber que é uma lista


def configure(app):
    app.admin = Admin(app, name='Live de Python admin')
    app.admin.add_view(MessageView(app.db.messages, 'Mensagens'))