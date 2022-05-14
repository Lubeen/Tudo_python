from inspect import ArgSpec


def ola(nome, cpf, idade=0, maiusculo=False):
    if maiusculo:
        msg = f"ola, {nome.upper()}!"
    else:
        msg = f"ola, {nome.lower()}, {cpf}, idade:{idade}!"

    print (msg)

pessoa = ['João','12345678901', 20]#variavel para passar os dados
nome, cpf, idade = pessoa #desencapacotamento de dados
ola(nome, cpf, idade)#passamos os dados para a função
#ou podemos fazer assim
ola(*pessoa)#passamos os dados para a função, se tiver asterisco * irá desempacotar listas
ola(**pessoa)#para desempacotar dicionários
#*args = captura todos os parametros posicionais
#**kwargs = captura todos os parametros nomeados
ola("joão", "12345678901", idade=20, maiusculo=True)
ola("joão", "12345678901", idade=20, maiusculo=False)
ola("joão", "12345678901", idade=20)
