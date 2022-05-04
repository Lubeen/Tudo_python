class Pizza:
    pedaços = 8

    def __init__(self, sabor):
        self.sabor = sabor

    def pegar_pedaço(self):
        """Método que retorna um pedaço da pizza e que é um metodo de instancia"""
        self.pedaços -= 1

    @classmethod
    def mudar_tamanho(cls, pedaços):
        cls.pedaços = pedaços

    @staticmethod
    def ingredientes():
        return "Massa, molho, queijo, tomate, alface, cebola, ovo, presunto, orégano"


class Mussarela(Pizza):#Reaproveitamento do codigo, mas de boa
    @staticmethod
    def ingredientes():
        return ['Massa, molho, queijo, tomate, alface, cebola, ovo, presunto, orégano']