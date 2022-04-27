from unicodedata import name
from flask import request, render_template
from flask import Blueprint

#Blueprint é parecido com flask

bp = Blueprint('site', __name__)#__name__ para indicar qual é o caminho importavel dele

@bp.route('/')
def index():
    return render_template(
        "index.html",
        name=request.args['name']
        )
