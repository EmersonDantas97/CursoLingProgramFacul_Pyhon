# Classificação dos módulos (built-in, de terceiros e próprios)
# Podemos classificar os módulos (bibliotecas) em três categorias:

# Módulos built-in: embutidos no interpretador.
# Módulos de terceiros: criados por terceiros e disponibilizados via PyPI.
# Módulos próprios: criados pelo desenvolvedor.

# Módulos built-in em Python são: math; os; svs; Random; datetime; re; collections.

# Aprendendo a utilizar a Matplotlib

import matplotlib.pyplot as plt

# Dados
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 3, 5]

# Criar um gráfico de linha
#plt.plot(x, y)
plt.bar(x, y) # Outro exemplo de grafico.

# Adicionar rótulos aos eixos
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

# Adicionar um título ao gráfico
plt.title('Exemplo de Gráfico de Linha')

# Mostrar o gráfico
plt.show()