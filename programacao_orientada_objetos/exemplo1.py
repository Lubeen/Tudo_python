# Abstracao
# tipos definidos pelo usuario 


class Fila:
      #  fila = []

   def __init__(self): #Metodo que traz atributos dinamicos
          self.fila = []

   def entrar(self, nome):
      self.fila.append(nome)
    
   
   def sair(self):
       return self.fila.pop(0)
        