
# 1. Crie as seguintes listas:

    # a) Lista de Nomes;

    # b) Lista de Números Pares


# a)
# nomes = ["João", "Maria", "Igor"]

# nomes.append("Pedro")

# # print(nomes)

# for nome in nomes:
#     print(nome)



# b)

from random import random


numeros = []
n = 10

for i in range(n):
    newNumber = int(random()* 100)
    
    if newNumber % 2 == 0:
        numeros.append(newNumber)

print(numeros)