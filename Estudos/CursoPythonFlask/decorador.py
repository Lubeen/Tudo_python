#Entregar para o usuario que esta chamando
#queremos entregar algo, geralmente produtos, dados, informações

#@login.required
def produto(nome):
    print(f"Produto: {nome}")

produto("Celular")

def produto(nome):
    #header()
    print(f"Produto: {nome}")
    #footer()

#Decorator = função que recebe função 
#automatizando
def header(function):
    def decorator(*args, **kwargs):#envelope, posso fazer coisas aqui usando uma função dentro de outra paara alterar a função
        print("header")
        return function()
    return decorator

#@footer
#@header



def x_salada(recheio):
    print(pao)
    print(recheio)
    print(pao)

x_salada("alface")

#mas é melhor ela ser generica

def lanche(recheio):
    print(pao)
    print(recheio)
    print(pao)

lanche("alface")

#mas eu posso deixar mais simples 

def pao(f):#eu tenho uma função e passo outra função
    def wrapper():#Eu envelopo essa função e chamo o recheio que eu quero mudar
        print('parte de cima')
        f() #eu passo a função com o recheio que quero
        print('parte de baixo')
    return wrapper #retorno o recheio modificado

#dessa forma só preciso chamar o decorator
#Essa função chamada lanche irá passar para pao como argumento sendo f
@pao
def lanche(recheio):
    print(f"{recheio}")
    print("hamburger")

    

#Classe

class Animal:
    #Atributo de classe
    planeta = "Terra"
    _animal_Nasceu=False #quanto tiver underline quer dizer que é privado dessa classe

    @property #posso chamar sem usar parenteses
    def nascido(self):#propertie
        return self.Nasceu

    def nascer(self):
        print("nascer, {self.planeta")
    def dormir(self):
        print("dormir")

class onivoro(Animal):#herda de Animal
    def comer(self):
        print("Estou toamando leite")

class mamifero(Animal):
    __slots__=["nome","idade"]#a classe só vai ter esse slots e nao vou poder adicionar
    def nascer(self):#sobrescrevendo metodos
        publico = 0
        _pŕotegida = 1
        __privada = 2
        print(f"Acabei de quebrar o ovo no {self.planeta}")
    
class Especial(mamifero, onivoro):#Herença multipla, não é boa pratica
    def __init__(self):
        self.mamifero = mamifero()
        self.onivoro = onivoro()
        print("Especial")

    def nascer(self):
        self.mamifero.nascer = self.mamifero.nascer()#Se for mudar o geral, se tiver metodo init precisa chamar assim

        print("Acabei de quebrar o ovo no {self.planeta}")

#properties