'''
        Método
É a lógica contida em uma classe para atribuir comportamentos(sequência de comandos), identificada por um nome.
Similar a funções e procedimentos.
Quando um método é executado dizemos que ele é invocado(chamado).
Exemplos de métodos: uma classe Pessoa pode ter os métodos nascer(), falar() e morrer().
É ideal que cada metodo só tenha uma função dentro da classe

        Criar Métodos
Sintaxe:
def nome_metodo(self, ...):
    codigo do metodo
    return valor

    

            Métodos utilitários
Métodos usados apenas dentro da classe, não sendo parte da interface pública usada pelo código cliente.
ou seja não acesso esse metodo diretamente do meu codigo principal do programa, esse metodo eu acesso atraves de outros metodos para realizar uma tarefa especifica

São acessados por outros métodos dentro do objeto para realizar tarefas especificas .

Devem preferencialmente ser nomeados com um underscore como prefixo.
Exemplo2: _dieta_especial_gato(self):


        Atributos ou Propriedades
Característica particular de uma ocorrência de uma classe, por exemplo o nome e a altura de uma pessoa.

Existem dois tipos principais de atributos ou variáveis:
Variável de Classe: Pertence à classe em si.
Variável de Instância: Pertence a cada objeto individualmente.
'''
#Variaveis de Classe e de Instancia

class Gato:
    tipo_animal = 'Felino' #atributo ou variavel de classe que pertence a classe gato

    def __init__(self, nome):
        self.nome = nome #Variavel de instancia
        self.tipo_animal = 'Felino' #Variavel de classe

Gato.tipo_animal = 'Pet' #altera o valor da variavel de classe
#não está atualizando as instancias
g1 = Gato('Lucas')
g2 = Gato('Luan')
g3 = Gato('Luben')

print(g1.nome)
print(g2.nome)
print(g3.nome)

g1.tipo_animal = 'Bichano'
print(g1.tipo_animal)
print(g2.tipo_animal)
print(g3.tipo_animal)
