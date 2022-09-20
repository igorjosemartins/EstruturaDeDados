
# from array import array


# 2) Crie as seguintes listas/array abaixo contendo, pelo menos 20 itens por lista:

#     a) Lista de Funcionários com os nomes e salários;
#     b) Lista de Contatos com os nomes e telefones;
#     c) Lista de Dólar Comercial com as datas, preço do dólar e preço do real.


# a)

from random import random


funcionarios = []

n = 20

for i in range(n):

    salario = int(random()* 1000)

    funcionarios.append(["João", salario])

print(funcionarios)
print(len(funcionarios))



# c) 

dolar = []
dolar.append([18/8/22, 5.17])
dolar.append([23/3/22, 5.45])
dolar.append([4/5/22, 5.29])