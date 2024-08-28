# Comando Hello World com o input, f-string e formatador de caracteres

nome = input("Digite seu nome: ") # Vai abrir uma linha de comando com string "Digite seu nome: " e esperar que seja digitado.

print(nome) # Vai apresentar o nome digitado. 

# Utilizando formatadores de caracteres
print("Olá %s, bem-vindo a disciplina de programação. Parabéns pelo seu primeiro Hello World!" % (nome))

# Utilizando f-string
print(f"Olá {nome}, bem-vindo a disciplina de programação. Parabéns pelo seu primeiro Hello World!")