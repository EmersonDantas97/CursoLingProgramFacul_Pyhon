# Aprendendo a utilizar métodos e classes em Python. 

# Definindo uma classe chamada pessoa
class Pessoa:
    
    # O método __init__ é um construtor, chamado quando um objeto da classe é criado.
    # Ele inicializa os atributos da classe.
    def __init__ (self, nome, idade, genero):

        # self é uma convenção em Python que se refere à própria instância da classe.
        # Os parâmetros nome, idade e gênero são passados durante a criação do objeto.
        # Eles são usados para inicializar os atributos da instância.
        self.nome = nome # Atribui o valor de nome ao atributo nome da instância.
        self.idade = idade # Atribui o valor de idade ao atributo idade da instância.
        self.genero = genero # Atribui o valor de gênero ao atributo gênero da instância.

    # O método cumprimentar retorna uma saudação com o nome da pessoa.
    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}!'
    
    # O método aniversário aumenta a idade da pessoa em 1.
    def aniversario(self):
        self.idade += 1

# Cria uma instância da classe “Pessoa” com os valores “João”, 30 e “Masculino” para nome, idade e gênero, respectivamente.
pessoa1 = Pessoa("João", 30, "Masculino")

# Chama o método “aniversário” na instância pessoa1 para aumentar sua idade em 1.
pessoa1.aniversario()

# Utilizando o metodo cumprimentar.
print(pessoa1.cumprimentar())

# Acessa o atributo idade atualizado da instância pessoa1 e imprime a nova idade.
print(f'Nova idade: {pessoa1.idade}') # Saída: Nova idade: 31

