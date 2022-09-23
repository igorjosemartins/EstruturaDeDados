# 2) Implemente o algoritmo que calcule a média pré-fixada em um array.

# Complexidade O(n²).

# array1 = [numero1, numero2, numero3, numero4] ??

# array2 = [numero1/divisor, numero2/divisor, numero3/divisor, numero4/divisor] ??

import random

array1 = []

n = 10

divisor = 5

for i in range(n):
    array1.append(random.randint(0, 100))


array2 = []

for j in range(n):
    array2.append(array1[j] / divisor)

print(array1)
print(array2)