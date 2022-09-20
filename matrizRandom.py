# 2) Criando lista com Array:
# Crie uma matriz 3 X 3 e adicione números inteiros aleatórios.
# Para cada elemento da matriz, verifique se é par ou impar.
# Caso seja impar adicione em uma nova matriz o valor 1, caso seja par, adicione 0.

# Exemplo:

# Matriz com números aleatórios

# 10 | 43 | 97 
# 56 | 28 | 72
# 83 | 39 | 91

# Matriz com 0s e 1s

# 0 | 1 | 1
# 0 | 0 | 0
# 1 | 1 | 1


import random

matrizRandom = []

matrizPI = []

n = 3

for i in range(n):
    row = []
    rowPI = []
    for j in range(n):
        numberRandom = random.randint(0, 100)
       
        row.append(numberRandom)
        
        if numberRandom % 2 == 0:
            numberRandom = 0
            rowPI.append(numberRandom)
        
        else:
            numberRandom = 1
            rowPI.append(numberRandom)

    matrizRandom.append(row)
    matrizPI.append(rowPI)

print(matrizRandom)
print(matrizPI)
