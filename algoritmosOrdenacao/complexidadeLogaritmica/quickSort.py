
# Ordenação rápida
# Algoritmo de ordenação eficiente
# Realiza menos comparações que outros algoritmos

# Lógica do algoritmo:
#   -> Utiliza um pivô
#   -> Divide o vetor no meio
#   -> Elementos menores que o pivô ficam a esquerda
#   -> Elementos maiores que o pivô ficam a direita
#   -> Repete esse processo até o subvetores ficarem com tamanho 1.

def quickSort(list, left, right):
    if (left < right):
        splitpoint = partition(list, left, right)
        quickSort(list, left, splitpoint -1)
        quickSort(list, splitpoint + 1, right)

def partition(list, left, right):
    pivot = list[right]
    i = left

    for j in range(left, right):
        if(list[j] <= pivot):
            list[i], list[j] = list[j], list[i]
            i = i + 1
    
    list[i], list[right] = list[right], list[i]
    return i

list = [26, 49, 38, 14, 58, 87, 35, 76]
 
quickSort(list, 0, len(list) - 1)

print("Quicksort: ", list)