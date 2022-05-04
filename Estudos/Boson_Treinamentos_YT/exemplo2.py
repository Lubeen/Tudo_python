"""
                Método Construtor

Metodo especial usado para inicializar um objeto instanciado.

Sintaxe:
def __init__(self, ...):
    codigo do metodo construtor

Quando a classe inclui o método __init__(), ele é automaticamente invocado quando ela é instanciada.
Quando a função estiver dentro de uma classe vamos chamar de MÉTODO


                O Identificador self

Sintaticamente, o parâmetro self identifica a instância sobre a qual um método é invocado. 
Ou seja, é uma referência à instância atual da classe(objeto).
É usado para acessar os membros que pertencem à classe em si.
Deve ser sempre o primeiro parâmetro usado na definição de um método.
"""

#metodo construtor serve para quando for instanciar a classe, ela ja ser inicializada com essas configurações ou caracteristicas
class Gato:
    '''Classe para trabalhar com gatos'''
    def __init__(self, nome):#parametro extra para interacao com usuario
        '''inicializa o objeto capturando o nome do animal'''
        self.nome = nome
        self.tipo_animal = 'Felino' # Essa variavel começou com self. para dizer que é uma variavel que pertence a classe gato, além disso ela será global
        print('Seu gato se chama', self.nome)
    
    def peso_gato(self, peso):
        '''Metodo para definir o peso do gato'''
        self.peso = peso #atributo interno self.peso que recebe o valor do parametro peso
        if self.peso > 10:
            print('Seu gato está muito pesado')
        elif self.peso < 5:
            print('Seu gato está muito magro')
        else:
            print('Seu gato está normal')
    
    def _dieta_especial_gato(self):#metodo utilitario, não tenho acesso direto :(
        '''Metodo para definir a dieta especial do gato'''
        self.msg = 'Tudo ok!'
        if (self.peso < 3):
            self.msg = 'Aumente a ração do seu gato'
        if (self.peso >= 5):
            self.msg = 'Diminua a ração do seu gato'
        return self.msg
    
    def dados_gato(self): #Preciso invocar o metodo utilitario em outro metodo 
        '''Metodo para mostrar os dados do gato'''
        print('Nome:', self.nome)
        print('Tipo:', self.tipo_animal)
        print('Peso:', self.peso)
        print('Dieta Especial:', self._dieta_especial_gato())


nome_gato = input('Digite o nome do seu gato: ')
g1 = Gato(nome_gato,)#não precisa de self, pois o self é interno

peso_gato = float(input('Digite o peso do seu gato, em kg:  '))
g1.peso_gato(peso_gato)
#g1 = Gato() #nome de objeto precisa ser curto, e com parenteses para indicar que precisa executar um metodo

g1.dados_gato()

