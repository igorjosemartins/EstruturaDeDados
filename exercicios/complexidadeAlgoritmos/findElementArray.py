# 3) Implemente o algoritmo que realize uma busca de um elemento em um
#    array e retorna o seu index. 

# Complexidade O(n).

import random

array = []

n = 5

for i in range(n):
    array.append(random.randint(0, 100))

print(array)

opt = int(input("Digite o elemento para buscar seu index: "))


for i in range(n):
    if opt == array[i]:
        print("Posição do elemento: ", array.index(opt))
        break

