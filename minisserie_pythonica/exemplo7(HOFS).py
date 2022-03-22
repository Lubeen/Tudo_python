# Funcoes de ordem superior ou HOFS
from typing import Callable, Any
# Twice essa funcao reaplica 
soma_2 = lambda val: val +2

def reaplica(func: callable, val: Any) -> Any:
    """Funcao que reaplica a funcao ao resultado da chamada."""
    return func (
        func(val)
    )


def seleciona(op: str) -> Callable:
    """Seleciona uma funcao, usando seu nome"""

    ops = {
        'soma': lambda x, y: x + y,
        'sub': lambda x, y: x - y
    }

    return ops[op]


palavras = [
'amar',
'transar',
'falar',
'abacaxi'
]


def take_cond(func, valores):
    for val in valores:
        if func(val):
            yield val
        else:
            break
        

