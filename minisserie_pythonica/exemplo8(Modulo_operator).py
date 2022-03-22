# Modulo Operator
from operator import add, mul, sub, itemgetter
from functools import reduce

# print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5]))
print(reduce(add, [1, 2, 3, 4, 5]))
print(reduce(mul, [1, 2, 3, 4, 5]))
print(reduce(sub, [1, 2, 3, 4, 5]))




palavras = [
'amar',
'transar',
'falar',
'abacaxi'
]

# sorted(palavras, key=lambda string: string[1])
sorted(palavras, key=itemgetter [1])

1 + 1
1 - 1
1 / 1
1 // 1
1 * 1
# 1 <op> 1