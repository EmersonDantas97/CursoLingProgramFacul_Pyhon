# As listas são mutaveis. 

cores = ['Vermelho', 'Azul', 'Verde', 'Amarelo', 'Roxo']

# Mudando o quarto item da lista
cores[3] = 'Cinza'

# Mostrando as cores em tela
for cor in cores:
    print(f'Posição: {cores.index(cor)} - Cores: {cor};')

