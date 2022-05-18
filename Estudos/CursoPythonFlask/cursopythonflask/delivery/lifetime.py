# #Contextos

# from distutils.log import debug
# from flask import Flask, request
# import flask
# app = Flask(__name__)

# ## 1 - Configuração

# ### Add configurações
# app.config["FOO"] = "bar"
# app.config["SQLALCHEMY_DB_URI"] = "sqlite:///:memory:"

# ### Registrar Rotas

# @app.route("/path")
# def path():
#     ...
# app.add_url_rule("/path", callable)

# ### Inicializar extensoes
# from flask_admin import Admin
# Admin.init_app(app)

# ### Registrar Blueprints
# app.register_blueprint(...)

# ### Add hooks
# @app.before_request(...)
# @app.after_request(...)
# @app.teardown_request(...)

# ### Chamar outras factories
# views.init_app(app)

# ## 2 - App Context

# ### App está pronto! 'app' está esperando wsgi chamar ele

# ### Testar 
# app.test_client
# debug
# objetos globais do flask (importar request, session, g, etc)
# Hooks
# from flask import current_app, g 

# ## 3 - Request Context 
# # usar globais do flask
# from flask import request

# request.args
# request.form

