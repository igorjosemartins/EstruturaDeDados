
# Ordenação por seleção
# Busca pelo menor elemento de cada iteração
# Lento para grandes entradas.

# Complexidade O(n2)

def selectionSort(list):
    for index in range(len(list)):
        min_index = index
        
        for j in range(index + 1, len(list)):
            if list[min_index] > list[j]:
                min_index = j
        list[index], list[min_index] = list[min_index], list[index]

list = [28, 44, 35, 12, 55, 85, 31, 96]

selectionSort(list)

print(list)