# Anotações de tipo
# Pesquisar pep-484
# mypy
# monkeytype

from numbers import Number
from typing import Any, Sequence, Union, List, Dict, Sequence, Text

Somavel = Union[Number,str,list]


def soma(x: Somavel, y: Somavel) -> Somavel:
    return x + y



def identidade(val: Any) -> Any:
    return val



def sum(l: List[Number]) -> Number:
    return sum(l)  



def cadastro_usuario(nome: str, idade: int, gostos: List[str]) -> Dict[str, Union[str, int, List[str]]]:
    return {
        'nome': nome,
        'idade': idade,
        'gostos': gostos,

    }



'''sequencia é qualquer coisa que são relacionadas a sequencia'''



def min(seq: Sequence):
    return min(seq)


def converte_para_reais(valor: Text): 
    bla = 0
