# Precisa instalar a biblioteca por meio do comando "pip install numpy" antes. Digitar diretamente no terminal

# Importando a biblioteca NumPy
import numpy as np

# Criando um arrau NymPy de numeros inteiros
meu_array = np.array([1,2,3,4,5])

# Colocando o array em tela
print("Array original: ")
print(meu_array)

# Realizando operacoes matematicas com array
aoquadrado_array = meu_array ** 2 # Elevando cada elemento ao quadrado
somar_os_elementos = np.sum(meu_array) # Calcula a soma de todos os elementos

#Imprimindo os resultados
print('\nArray ao quadrado:')
print(aoquadrado_array)
print('\nSoma dos elementos:')
print(somar_os_elementos)

# Acessando os elementos array
elemento_do_index2 = meu_array[2] # Acessando o elemento de index 2
print(f'\nElemento de index 2 é o: {elemento_do_index2}')



