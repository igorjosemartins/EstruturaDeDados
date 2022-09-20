# 1) Crie uma pilha para armazenar nomes de
# documentos. Cada documento terá um nome.

class Stack:
    def __init__(self):
        self.stack = []

    # adicionar um valor a pilha
    def append(self, data):
        # se o dado não estiver na pilha:
        # botamos o dado
        if data not in self.stack:
            self.stack.append(data)
            return True
        # se não, falso
        else:
            return False

    # retira o último elemento colocado na pilha
    def pop(self):
        # se o tamanho da pilha for menor igual a 0:
        # a pilha está vazia
        if len(self.stack) <= 0:
            return "Pilha vazia"
        # se não, retiramos o ultimo elemento
        else:
            return self.stack.pop()

    # loop para mostrar a pilha
    def printStack(self):
        # se a pilha é vazia:
        # ela está vazia
        if self.stack is None:
            print("Pilha vazia")
        # loop para mostrar a pilha
        # para cada indice dentro do tamanho da pilha:
        # print o dado da pilha na posição "i"
        for i in range(len(self.stack)):
            print(self.stack[i])