# Aprendendo sobre herança em Python

class Animal:
    def __init__(self, nome):
        self.nome = nome
    def fazer_barulho(self):
        pass

class Cachorro(Animal):
    def fazer_barulho(self):
        return "Latir!"

class Gato(Animal):
    def fazer_barulho(self):
        return "Miar!"

rex = Cachorro("Rex")
zoe = Gato("Zoe")

print(f'Nome do cachorro é {rex.nome} e o que ele faz é {rex.fazer_barulho()}')
print(f'Nome do gato é {zoe.nome} e o que ela faz é {zoe.fazer_barulho()}')