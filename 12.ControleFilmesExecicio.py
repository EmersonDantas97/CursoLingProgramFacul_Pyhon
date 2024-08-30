# Lista de filmes para classificacao. 

filmes = ['Filme 1', 'Filme 2', 'Filme 3', 'Filme 4', 'Filme 5']

# Colocando tracos para ficar visual
print('****************************************************\n')

# Mensagens de voas vindas.
print('Bem-vindo à classificação de filmes!')
print('Você tem cinco filmes para classificar.')
print('Digite 0 a qualquer momento para parar. \n')

# Loop para iterar sobre cada filme da lista.
for filme in filmes:
    
    #Solicita classificacao do usuario.
    classificacao = input(f'Como você classificaria o filme {filme}? Coloque uma nota de 1 à 5 ou digite 0 para sair.\n')

    # Verificando se o usuario digitou 0 para parar.
    if classificacao == '0':
        print("Que pena, você não irá mais classificar os filmes!\n")
        break

    # Convertendo a classificacao para um numero inteiro.
    classificacao = int(classificacao)

    # Validando para ver se a classificacao esta dentro de um intervalo valido.
    if classificacao < 1 or classificacao > 5:
        # Apresentando ao usuario a mensagem de que ele inseriu um valor errado.
        print('Número incorreto! Por favor, digite um número de 1 a 5 para classificar!\n')
    else:
        # Exibe a clasificacao e passa para o proximo filme.
        print(f'Você classificou o filme {filme}, com {classificacao} estrelas.\n')

# Mensagem de agradecimento ao finalizar
print('Obrigado por classificar os filmes!\n')
print('****************************************************')


    




