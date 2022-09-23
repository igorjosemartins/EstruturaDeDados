
# 1) Crie uma pilha para armazenar nomes de documentos. 
# Cada documento terá um nome.


class Stack:
    def __init__(self):
        self.stack = []

    def append(self, data):
        if data not in self.stack:
            self.stack.append(data)
            return True
        else:
            return False

    def pop(self):
        if len(self.stack) <= 0:
            return "Pilha vazia"
        else:
            return self.stack.pop()

    def printStack(self):
        if self.stack is None:
            print("Pilha vazia")
        
        for i in range(len(self.stack)):
            print(self.stack[i])

stack = Stack()

stack.append("Documentos")
stack.append("Downloads")
stack.append("Músicas")

#stack.pop()

stack.printStack()