# Foco no dicionario em Python, são objetos que associam chaves a valores, são mutaveis. 

dicionario_1 = {}

# Exemplo 1 de criação de dicionario
dicionario_1['Nome'] = "Maria"
dicionario_1['Idade'] = 25

# Exemplo 2 de criação de dicionario
dicionario_2 = {'Nome': 'Maria', 'Idade': 25}

# Exemplo 3 de criação de dicionario. Utilizando lista de tuplas.
dicionario_3 = dict([("Nome", 'Maria'),("Idade", 25)])

# Exemplo 4 de criação de dicionario. Usando a função built in zip() em duas listas, uma para as chaves e outras para os valores
dicionario_4 = dict(zip(['Nome', 'Idade'],['Maria', 25]))

# Realizando se todas as construcoes feitas de dificionario sao iguais
print(dicionario_1 == dicionario_2 == dicionario_3 == dicionario_4)
print(dicionario_1)
print(dicionario_2)
print(dicionario_3)
print(dicionario_4)












