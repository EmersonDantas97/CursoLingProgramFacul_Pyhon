# Estruturas logicas e operadores booleanos

# E = and
# OU = or
# NÃO = not

idade = int(input("Digite sua idade: "))

if idade < 18:
    print("Menor de idade.")
elif idade >= 18 and idade < 65:
    print("Adulto.")
else:
    print("Idoso.")