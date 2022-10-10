# Ordenação por mistura
# Algoritmo de ordenação eficiente
# Paradigma: dividir para conquistar

# Complexidade: O(n log n) 2

# Lógica do algoritmo:
#   -> Vetor original é dividido em dois recursivamente em cada rodada
#   -> Divide até o tamanho do subvetor seja 1
#   -> Junta-se os subvetores, a fim de ordenar o conjunto inteiro.

def mergeSort(list, left, right):
    if(left < right):
        middle = int((left + right) / 2)
        mergeSort(list, left, middle)
        mergeSort(list, middle + 1, right)
        merge(list, left, middle, right)

def merge(list, left, middle, right):
    # cria vetor vazio com tamanho do subvetor
    vector = [None] * (right - left + 1)
    i = left
    j = middle + 1
    k = 0

    while(i <= middle and j <= right):
        if(list[i] < list[j]):
            vector[k] = list[i]
            i = i + 1
        else:
            vector[k] = list[j]
            j = j + 1
        k = k + 1

    while(i <= middle):
        vector[k] = list[i]
        i = i + 1
        k = k + 1

    while (j <= right):
        vector[k] = list[j]
        j = j + 1
        k = k + 1
    
    for l in range(0, k):
        list[left + l] = vector[l]

list = [26, 49, 38, 14, 58, 87, 35, 76]

mergeSort(list, 0, len(list) - 1)

print(list)