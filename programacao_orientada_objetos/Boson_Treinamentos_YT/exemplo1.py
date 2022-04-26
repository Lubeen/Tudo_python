#Sintaxe para a criação de classes:
"""
Sintaxe simplificada:
class NomeDaClasse: #Cabeçalho da classe
    pass #classe vazia(ainda)

print(type(NomeDaClasse)) #classe do elemento

Especificando membros:

class NomeDaClasse: #Cabeçalho da classe
    ''' docstring (opcional) '''
    dado = valor #dado de classe compartilhado (atributo de classe)
    def metodo_construtor # metodo construtor, metodo especial toda classe tem 
        codigo metodo construtor
    def metodo(self, ...) #metodo geral
        self.membro = valor # dado geral ('self')

"""

class Cubo:
    '''Classe para calcular o cubo de um número'''
    def __init__(self, valor): #metodo construtor da classe é um metodo automatico
        self.x = valor #variavel global, por causa do self
        print('objeto criado!')
    def calcula_cubo(self):#calculo, só recebe self para indicar a classe a qual ele pertence
        #os metodos precisam ser escritos por padrão com as iniciais em minusculo e separados por underline
        cubo = self.x ** 3 #Cubo não tem cubo.self pois self ja aparece depois, então cubo é local
        return 'Cubo calculado: ' + str(cubo)


print(type(Cubo))

teste = Cubo(6)
c = teste.calcula_cubo()
print(c)