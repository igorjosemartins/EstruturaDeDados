
class Queue:
    def __init__(self):
        self.items = list()

    # adicionar um elemento a fila
    def enqueue(self, item):
        # se o elemento digitado não estiver na fila
        if item not in self.items:
            # insira ele na posição (tamanho da lista), elemento digitado
            self.items.insert(len(self.items), item)

    # retirar um elemento da fila
    def dequeue(self):
        # se o tamanho da lista for maior que 0
        if len(self.items) > 0:
            # tire o primeiro elemento que entrou na lista = [0]
            return self.items.pop(0)
    
    # tamanho da lista
    def size(self):
        return len(self.items)