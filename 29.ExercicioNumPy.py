# ?Importando as bibliotecas necessarias
import numpy as np

# Dados dos participantes
participantes = [
    {
        'nome': 'Alice',
        'localizacao': 'EUA',
        'afiliacao': 'Universidade A',
        'interesses': ['Fisica', 'Astronomia']
    },
    {
        'nome': 'Bob',
        'localizacao': 'BR',
        'afiliacao': 'Universidade B',
        'interesses': ['Biologia', 'Astronomia']
    },
    {
        'nome': 'BCharlie',
        'localizacao': 'IN',
        'afiliacao': 'Universidade C',
        'interesses': ['Quimica', 'Engenharia']    
    }
    # Adicionar mais participantes caso necessario
]

# Usando sets para identificar diferentes regiões dos participantes
regioes = set(participante['localizacao'] for participante in participantes)

# Usando um dicionario para categorizar as afiliacoes
afiliacoes = {}

for participante in participantes:
    afiliacao = participante['afiliacao']
    if afiliacao not in afiliacoes:
        afiliacoes[afiliacao] = []
    afiliacoes[afiliacao].append(participante['nome'])

# Usando Numpy para analisar áreas de interesse
areas_de_interesse = np.array([interesse for participante in participantes for interesse in participante['interesses']])   
interesses_unicos, contagem = np.unique(areas_de_interesse, return_counts=True)
area_mais_popular = interesses_unicos[np.argmax(contagem)]

# Resultados
print("Regiões dos participantes: ", regioes)
print("Afiliações dos participantes: ")
for afiliacao, nomes in afiliacoes.items():
    print(f'{afiliacao}: {', '.join(nomes)}')

print(f'Área de interesse mais popular: ', area_mais_popular)



