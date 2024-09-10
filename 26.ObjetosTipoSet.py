# É um conjunto, representa uma colecao de elementos unicos.

# Comandos add(), in e remove()

meu_conjunto = set()

# Adicionando elementos ao conjunto
meu_conjunto.add(10)
meu_conjunto.add(20)
meu_conjunto.add(30)
meu_conjunto.add(500)

# Imprimindo o conjunto
print(meu_conjunto)

# Verificando se um elemento esta no conjunto e removendo caso esteja
elemento_a_remover = int(input("Digite qual o elemento deseja remover: "))

if elemento_a_remover in meu_conjunto:
    print(f'O elemento {elemento_a_remover} está no conjunto!')
else:
    print(f'O elemento {elemento_a_remover} NÃO está no conjunto!')

# Removendo o elemento
meu_conjunto.remove(elemento_a_remover)

# Imprimindo o conjunto atualizado
print(meu_conjunto)



