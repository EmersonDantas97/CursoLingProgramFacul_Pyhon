# Criando funcao e par.

def e_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

numero = int(input('\nDigite um numero que vem a sua mente: '))

if e_par(numero):
    print(f'\n{numero} é par!')
else:
    print(f'\n{numero} é impar!')
