'''
Métodos: Acesso a Campos = atributos
Os campos denotam o estado de um objeto e o estado deve ser alterado somente pela interação com 
métodos pré-definidos que controlam o comportamento do objeto.
Isso ajuda a preservar a integridade dos dados.
Conseguimos isso por meio do emprego de métodos especiais.

        Métodos Getter e Setter
Métodos setter:usados para alterar ou inserir valores nos membros de dados, geralmente atributos.
exemplos: setNome(), setDataNascimento(), setSalario(), setCargo()
Métodos getter: usados para recuperar(ler) valores dos membros de dados ou armazenados nos objetos.
exemplos: getNome(), getDataNascimento(), getSalario(), getCargo()

como regra, um objeto só pode ter seus dados manipulados com o uso de setters e getters especificados
'''

class Teste():
    def __init__(self, valor):
        self.x = valor
        print('objeto criado!')

  
    def get_valor(self):#esse metodo retorna o valor do atributo x
        '''Método getter para retornar o valor do atributo x:'''
        return self.x
    
    def set_valor(self, v):#esse metodo altera o valor do atributo x
        '''Método setter para alterar o valor do atributo x:'''
        self.x = v
    
teste = Teste(10)
print('Valor do objeto:', teste.get_valor())

val = int(input('Digite um valor: '))
teste.set_valor(val)
print('Valor do objeto após atribuição', teste.get_valor())
