# Lista de notas dos estudantes
notas = [7.5, 8.0, 9.0, 7.0]

# Funcao regular para calcular a media
def calcular_media(notas):
    total = sum(notas)
    media = total / len(notas)
    return media

# Funcao lambda para arredondar a media para duas casas decimais
arrendondar_media = lambda media: round(media, 2)

# Calculando a media
media = calcular_media(notas)
media_arredondada = arrendondar_media(media)

# Verificando se o estudante foi aprovado
situacao = "Aprovado" if media_arredondada >= 7.0 else "Reprovado"

# Apresentando resposta ao usuario
print(f'Notas do estudante: {notas}.')
print(f'Média das notas: {media_arredondada}.')
print(f'Situação do estudante: {situacao}.')
