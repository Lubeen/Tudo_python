#ABstracao da abstracao para reutilizar codigo
# Herdando pizzas
from exemplo2 import Pizza #pai

class Mussarela(Pizza):#filho, herdou
    ...
class Calabresa(Pizza):#filho, herdou
    ...
class MeioAMeio(Mussarela, Calabresa):#Polimorfismo
        ...