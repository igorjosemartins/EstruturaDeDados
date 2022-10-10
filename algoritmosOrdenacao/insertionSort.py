
# Ordenação por inserção
# Algoritmo criado com base em um jogo de cartas
#   -> Cada nova carta, deve ser colocada na posição
#      correta

# • Complexidade O(n2).

def insertionSort(array):
    for i in range(1, len(array)):
        j = i - 1
        key = array[i]
        while array[j] > key and j >= 0:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key

list = [6, 5, 3, 1, 8, 7, 2, 4]

insertionSort(list)

print(list)