# Aprendendo a utilizar os controles de repições.

for numero in range(3, 11):
    if numero % 2 == 0:
        print("O primeiro par encontrado é: ", numero)
        break # Para execucao do codigo.

for numero in range(1, 11):
    if numero == 5:
        continue # Pula execucao do codigo.
    print(numero)

