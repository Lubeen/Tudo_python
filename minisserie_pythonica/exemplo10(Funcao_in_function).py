# funcoes aninhadas
# funcoes dentro de funcoes
# Function in function


def func():
    def func_():
        ...
        
    ...

from difflib import ndiff
from typing import List, NoReturn
import readline


def file_diff(file_1: str, file_2: str) -> NoReturn:
    def read_file(file: str) -> List:
        """Abre o arquivo, ignorando a linha inicial e a linha final"""
        return [e.replace (',' , '')
        for e in open(file).readlines()[1:-1]
        ]

    content_1 = read_file(file_1).readlines()
    content_2 = read_file(file_2).readlines()

    print(''.join(ndiff(content_1, content_2)))