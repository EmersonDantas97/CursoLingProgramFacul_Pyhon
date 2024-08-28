# Programinha para avaliar nota de alunos.

# Nas linhas abaixo sera utilizado o comando int, pois Python interpretara como string, caso nao utilizado. 
nota_1 = int(input("Digite a primeira nota: "))
nota_2 = int(input("Digite a segunda nota: "))
nota_3 = int(input("Digite a terceira nota: "))
nota_4 = int(input("Digite a quarta nota: "))

# Verificando a media.
media = (nota_1 + nota_2 + nota_3 + nota_4) / 4

# Condicao para aprovacao do aluno.
if media >= 6:
    situacao = "Aprovado"
else:
    situacao = "Reprovado"

# Aprensentando os resultados
print(f'A média das notas é {media}.')
print(f'A situação do aluno é {situacao}.')

