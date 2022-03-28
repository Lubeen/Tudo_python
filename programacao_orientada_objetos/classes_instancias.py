# Exemplo de uso de cls e self:

class Fila: #criacao de uma abstracao de dado.
    c_fila = []

    @classmethod 
    def c_entrar(cls, nome):
        cls.c_fila.append(nome) #manipulacao da abstracao de dado
        print(cls.c_fila)

    def __init__(self): #Manipulacao do exemplo, ou instancia, representada pelo tipo de dado
        self.s_fila = []

    def s_entrar(self, obj):
        self.s_fila.append(obj)
        print(self.s_fila)