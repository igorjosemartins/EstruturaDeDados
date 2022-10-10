
# Ordenação por monte
# Ordenação com Árvore-Heap
# Estrutura de dados que tem como base uma estrutura em árvore
# Na prática, a ordenação é feita em um vetor.

# Complexidade: O(n log n) 2

# Desvantagens:
#   - Construir a árvore-heap pode consumir muita memória.

# Vantagem:
#   - Para dados imprevisíveis, pode ser mais vantajoso por ser previsível 
#   - em termos de tempo de execução.

# • Heap:
# – Árvore Binária;
# – Balanceada e justificada a esquerda.

# • Árvore-Heap:
# – Nodo pai será sempre maior que os nodos filhos.


# cria a árvore heap
def heapify(list, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and list[i] < list[left]:
        largest = left

    if right < n and list[largest] < list[right]:
        largest = right
    
    if largest != i:
        list[i], list[largest] = list[largest], list[i]
        heapify(list, n, largest)

    # chama o método heapify
    def heapSort(list):
        n = len(list)

        # n//2 = divisão inteira
        for i in range(n//2, -1, -1):
            heapify(list, n, i)

        for i in range(n - 1, 0, -1):
            list[i], list[0] = list[0], list[i]
            heapify(list, i, 0)