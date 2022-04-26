# Herdando pizzas
# A partir da herança podemos gerar uma caracteristica da programacao orientada a objetos que se chama polimorfismo

class Pizza:
    pedaços = 8

    @classmethod
    def mudar_tamanho(cls, pedaços):
        cls.pedaços = pedaços

class Mussarela(Pizza):
    ...

class Calabresa(Pizza):
    ...
class MeioAMeio(Mussarela, Calabresa):
    ...




    