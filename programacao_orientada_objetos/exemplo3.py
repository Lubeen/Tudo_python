#classmethod vs method


class CLass:
    @classmethod
    def _classmethod(*args):#funcao especial ou metodo, ela interaje com o atributo da classe e pode altera-la
        print(args)

    def _method(*args):#funcao ou metodo para ser chamado, porem não é igual a classmethod
        print(args)