# Primeiro modo
import math

math.sqrt(25)
math.log2(1024)
math.cos(45)
# Perceba que eu tenho que digitar o nome da biblioteca antes do metodo.

# Segundo modo
import math as m

m.sqrt(25)
m.log2(1024)
m.cos(45)
# Perceba que eu tenho que digitar o apelido que eu dei a biblioteca antes do metodo.

# Terceiro modo
from math import sqrt, log2, cos

sqrt(25)
log2(1024)
cos(45)
# Perceba que eu apenas chamo o metodo, sem ser necessário falar o nome da bilbioteca, pois eu importei 

# somente os metodos da biblioteca.
