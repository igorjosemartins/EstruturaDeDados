
class Node:
    # construtor (dado, ponteiro)
    def __init__(self, data):
        # próprio dado
        self.data = data
        # referência como vazio, pois iremos atribuir ela dps
        self.next = None
    
class linkedList:
    
    def __init__(self):
        # cabeça (primeiro elemento como vazio)
        self.head = None

    def append(self, data):
        newNode = Node(data)

        if self.head == None:
            self.head = newNode
            return
        
        currentNode = self.head

        while currentNode.next:
            currentNode = currentNode.next
        
        currentNode.next = newNode
        return