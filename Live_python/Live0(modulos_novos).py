from itertools import count, cycle, repeat
from _collections_abc import MutableSequence


def func(x):
    return x + 2


# Conta sempre o proximo
a = count(1)
# Conta até o ultimo e volta
b = cycle([1, 2, 3, 4])
# Repete algo sempre
c = repeat(10)
# Map é uma funcao que recebe uma funcao ou sequencia como arguemento e é uma saida para um for
# Um exemplo para facilitar o entendimento de map temos essa lista
lista = []
for x in[1, 2, 3, 4]:
    lista.append(func(x))

# Mesma logica e no map ele retorna um iterator do tipo lazy
map(func, [1, 2, 3, 4])
# Se colocar dentro de uma lista ele retorna o mesmo resultado
list(map(func, [1, 2, 3, 4]))

# filter(func,[1,2,3,4])
# Out[6]: <filter at 0x7f2e2c725880>
# list(filter(func,[1,2,3,4]))
# Out[7]: [1, 2, 3, 4]

# for x in enumerate('Luan'):
#     print(x)
#
# (0, 'L')
# (1, 'u')
# (2, 'a')
# (3, 'n')

# for x, y in enumerate('Luan'):
#     print(x,y)
#
# 0 L
# 1 u
# 2 a
# 3 n




