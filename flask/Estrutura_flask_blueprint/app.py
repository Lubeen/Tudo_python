from Estrutura_flask_blueprint.ext.site_blueprints.main import bp
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.register_blueprint(bp)
    return app