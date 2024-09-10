# As listas são mutaveis. 

cores = ['Vermelho', 'Azul', 'Verde', 'Amarelo', 'Roxo']

# Mudando o quarto item da lista
cores[3] = 'Cinza'

# Antes de colocar todos os itens da lista em minuscula
print(f"Antes da list coprehension = {cores}")

cores = [item.lower() for item in cores]

# Depois de colocar todos os itens da lista em minuscula
print(f"\nDepois da list coprehension = {cores}")
