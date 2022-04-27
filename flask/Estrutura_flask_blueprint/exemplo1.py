'''
Em um projeto flask é interessante estruturar as pastas para ficar tudo organizado e facilitar o desenvolvimento do codigo
logo na raiz do seu projeto crie arquivos chamados app.py, main.py, __init__.py e por fim 
crie pastas chamadas templates, static e config.
setup.py = é onde instalamos o projeto
app.py = arquivo principal do projeto serve para flask run
main.py = arquivo principal do projeto
__init__.py = arquivo que transforma a pasta em um pacote python para que seja importavel por ides ou ferramentas
templates = pasta que contem os templates do projeto
static = pasta que contem os arquivos estaticos do projeto, js, css, imagens, etc
config = pasta que contem os arquivos de configuracao do projeto
pasta tests = precisa estar fora da pasta do projeto para que o teste funcione corretamente

Também é interessante ter extensões para criar interface no projeto
por exemplo com flask_admin, dyna_conf
ou seja criar uma pasta para colocar as extensoes

MVC x Aplicattion Factory

Aplicattion Factory = É somente a abordagem da gente criar funções que retornam objetos 
                                                                        ex: def create_app():
                                                                            app = Flask(__name__)
                                                                            return app
poderia ser assim: 
ex: app = Flask(__name__) # aqui vai executar junto com o programa
Isso permite que aquilo se torne lazy, ou seja, aquilo vai executar só no futuro no run time

MVC é outra historia, Model View Controller é uma escolha de arquitetura de software
Quando for criar uma pasta pare e pense essa responsabilidade é de quem, do visual=beleza e ordem ou do model=dados ou do controller= regra de negocio
                                                           
'''