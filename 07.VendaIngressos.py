# Maquina de venda de ingresso no cinema

# Solicita a idade do cliente
idade = int(input("Por favor, digite sua idade: "))

# Verifica a idade para sugestao de filmes
if idade < 12:  
    print("Recomendamos o filme infantil FILME 1.")
elif 12 <= idade < 18:
    print("Recomendamos o filme adolescente FILME 2.")
else:
    print("Recomendamos o emocionante FILME 3.")

# Verifica a quantidade de ingressos
qtd_ingressos = 0

if qtd_ingressos > 0:
    print("Os ingressos estão disponíveis. Divirta-se no cinema!")
else:
    print("Desculpe, mas todos os ingressos estão esgotados para esta filme!")
