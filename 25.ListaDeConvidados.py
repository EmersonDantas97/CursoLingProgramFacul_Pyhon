# Utilizando os conteudos dos arquivos 19.py ao 24.py em um exercicio.

convidados = ('Alice', 'Maria', 'Jose', 'Bruna', 'Barbara', 'Adriano')

confirmados = ['Alice', 'Bruna']

nao_confirmados = [convidado for convidado in convidados if convidado not in confirmados]

# Exibindo convidados que ainda não confirmaram 
print('Convidados que ainda não confirmaram:')

for pessoa in nao_confirmados:
    print(pessoa)

print('Favor enviar convite novamente para os convidados acima!')