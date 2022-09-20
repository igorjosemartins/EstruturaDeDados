# 4) Crie um programa que calcule o dobro dos valores da diagonal principal de uma matriz 3X3.

matriz = [[2, 0, 0], [0, 2, 0], [0, 0, 2]]

n = len(matriz)

for i in range(n):
    for j in range(n):
        if i == j:
            matriz[i][j] *= 2

print(matriz)