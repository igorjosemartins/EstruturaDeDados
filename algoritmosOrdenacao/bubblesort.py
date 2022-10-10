
# Algoritmo de ordenação popular
# • Estratégia:
#   -> Elementos maiores do vetor são movidos para o
#      final do vetor, como se fosse bolhas leves.

# • Complexidade: O(n2).

def bubbleSort(array):
    n = len(array)
    swapped = False
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if not swapped:
            return

list = [5, 1, 2, 4, 8]

bubbleSort(list)

print(list)
