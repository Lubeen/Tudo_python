#blueprint = plugin
#o pyhton admin é parecido com um blueprint
from flask import Blueprint, render_template, request, abort, current_app

#Request só funciona dentro de uma view
bp = Blueprint('contact', __name__, url_prefix='/contact')
#não posso importar nem criar um novo em blueprint

@bp.route('/', methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        return render_template('contact.html')

    #Processar dados
    name = request.form['name']
    message = request.form['message']
    print(request.form)
    return "Sua mensagem foi enviada com sucesso!"

    #Validar
    if not name or not message :
        abort(400, 'Mensagem invalida!')

    #Banco de dados
    current_app.db.messages.insert_one({'name': name, 'message': message})


    
#factories
def configure(app):
    app.register_blueprint(bp)