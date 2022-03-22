# Funcoes parciais
from operator import add, itemgetter, mul, itemgetter
# produto de Higher order functions com produto de objeto de primeira classe
from functools import partial, reduce

# def soma_2(x):
    # return x + 2
# soma_2 = lambda x: x + 2

# Com a funcao parcial
soma_2 = partial(add, 2)
mul_2 = partial(mul, 2)

reduce(add, [1, 2, 3, 4, 5])
reduce(mul, [1, 2, 3, 4, 5])

somatorio = partial(reduce, add)
multiplicatio = partial(reduce, mul)
mul_2_all = partial(map, mul_2)
ordenar_1 = partial(sorted, key=itemgetter(1))


def func(a,b,c,d,e ,database=None):
    return database, a, b, c, d, e


func_postgres = partial(func, database='postgres')
func_maria = partial(func, database='mariaDB')
func_mongo = partial(func, database='mongoDB')
