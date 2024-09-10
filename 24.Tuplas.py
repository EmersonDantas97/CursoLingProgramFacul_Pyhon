# São semelhantes as listas, porém a única diferenca é que são imutáveis. Uma vez criadas não podem ser alteradas.

cores = ('Vermelho', 'Azul', 'Verde', 'Amarelo', 'Roxo')

# Mudando o quarto item da lista
cores[3] = 'Cinza'

# Mostrando as cores em tela
for cor in cores:
    print(f'Posição: {cores.index(cor)} - Cores: {cor};')

# Executando os codigos acima, vai dar erro, pois a tupla não permite ser editada.