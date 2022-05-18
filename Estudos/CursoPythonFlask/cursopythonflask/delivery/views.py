#Extensão Flask


def init_app(app):
    """Inicialização de extensões"""

    @app.route('/')
    def index(): #views
        return '<h1>Hello</h1>'

    @app.route('/home')
    def home():
        return '<h1>Hello, im home</h1>'