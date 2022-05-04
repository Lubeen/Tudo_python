# Herdando pizzas
# A partir da herança podemos gerar uma caracteristica da programacao orientada a objetos que se chama polimorfismo



class Pizza:
    pedaços = 8

    @classmethod
    def mudar_tamanho(cls, pedaços):
        cls.pedaços = pedaços

@staticmethod
def ingredientes():
    return ingredientes()


class Mussarela(Pizza):
    

    @staticmethod
    def ingredientes():
        return ['Oregano', 
                'Queijo',
                'Tomate',
                'Azeitona']


class Calabresa(Pizza):
    ...
class MeioAMeio(Mussarela, Calabresa):
    ...




    