# 1) Implemente o algoritmo de busca do maior valor de um array.

# Complexidade: O(n)

import random

array = []

n = 5

for i in range(n):
    
    array.append(random.randint(0, 100))

    maxValue = array[0]
    if maxValue < array[i]:
        maxValue = array[i]

print(array)

print("O maior valor do array é: ", maxValue)