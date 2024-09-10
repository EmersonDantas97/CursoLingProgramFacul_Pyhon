# Criando uma calculadora que valida o desconto dado no produto

# Recebendo o valor do produto
valor_produto = float(input("Digite o valor do produto:   "))

# Recebendo a porcentagem de desconto do produto
percentual_desconto = float(input("\nDigite a porcentagem de desconto dado no produto:   "))

# Caso o desconto seja maior ou menor do que devido, sera exibido a msg ao usuario
if percentual_desconto < 0 or percentual_desconto > 100:
    print("Desconto inválido! Tente novamente!")
else:
    desconto = valor_produto * (percentual_desconto / 100)
    valor_final = valor_produto - desconto
    print(f'O valor do produto com desconto é R$ {valor_final}.')

