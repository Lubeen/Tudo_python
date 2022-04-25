

from Curso_flask import app 


if __name__ == '__main__':
    app.run(debug=True) #por segurança se for o arquivo principal execute


from Curso_flask.app.controllers import default #Precisa importar depois de executar o run
