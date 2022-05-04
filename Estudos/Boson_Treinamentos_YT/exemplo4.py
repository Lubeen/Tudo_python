'''
            Objeto
Ocorrência específica de uma classe - 'instancia de classe'
Representa entidades do mundo real, como carros, pessoas, contas correntes, etc., e outros conceitos,
como gráficos(círculos, quadrados, cones, esferas, etc.)
Tem características próprias(atributos) e executa ações (métodos), provenientes da classe que originou o objeto.

        Criar instâncias: os objetos
Para podermos usar os métodos e atributos de uma classe precisamos primeiro derivar um objeto dessa classe.

Esse processo se chama instanciação.

Sintaxe:
nomeObjeto = NomeClasse(parametros)

A atribuição cria uma nova instância da classe, e atribui o objeto criado à variável local nome objeto.
'''

class CalcCubo:
    '''Classe para calcular o cubo de um número'''
    def __init__(self, valor): #metodo construtor da classe é um metodo automatico
        self.x = valor #variavel global, por causa do self
        print('objeto criado!')
    def calcula_cubo(self):#calculo, só recebe self para indicar a classe a qual ele pertence
        #os metodos precisam ser escritos por padrão com as iniciais em minusculo e separados por underline
        self.cubo = self.x ** 3 #Cubo não tem cubo.self pois self ja aparece depois, então cubo é local
        return 'Cubo calculado: ' + str(self.cubo)

num = int(input('Entre com um número:'))
objCubo = CalcCubo(num)  # instanciar a classe
cubo = objCubo.calcula_cubo()#Precisamos acessar o metodo atraves do objeto,
#apos isso só criamos a variavel para receber o valor que a funcao retorna
num = int(input('Entre com outro número:'))
objCubo2 = CalcCubo(num)  # instanciar a classe novamente
cubo2 = objCubo2.calcula_cubo() #passamos o retorno da funcao para a variavel cubo2
print(cubo)
print(cubo2)


#print(type(CalcCubo))#tipo de dado customizavel
#print(type(objCubo))#objeto criado a partir da classe
