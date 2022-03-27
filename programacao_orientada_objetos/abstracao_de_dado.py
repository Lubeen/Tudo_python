# Abstracao
# tipos definidos pelo usuario 


class Fila: # nos temos uma classe que representa um molde de todos os passaros, o motivo da primeira letra ser maiscula em classe é por causa das boas praticas do python
    estado = 'indefinido' # O motivo de estar com 4 espaçamentos é por causa que o estado que esta dentro de fila somado com o fato de que estado é uma definifição de classe resultado em 4 espaçamentos 
    
    def __init__(self): #nos temos metodos padrao
       self.fila = []

    def entrar(self, nome): #e metodos especificos criados pelo programador
        self.fila.append(nome)    

    def sair(self):#esses metodos recebem parametros que sao suas difinicoes, porem preciso declarar que a funcao recebe ela mesma para que o sistema entenda que se trata de uma funcao dela mesma
        self.fila.pop(0)