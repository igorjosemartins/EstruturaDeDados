
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        
        if data:
            self.data = data
        else:
            self.data = None

    def insert(self, data):
        if self.data:
            # se o dado for menor que o primeiro 
            if data < self.data:
                # verificando se existe um dado à esquerda
                if self.left is None:
                    # se não tiver, cria
                    self.left = Node(data)
                # se tiver insere o dado na esquerda
                else:
                    self.left.insert(data)

            # se o dado for menor que o primeiro
            elif data > self.data:
                # verificando se existe um dado à direita
                if self.right is None:
                    # se não tiver, cria
                    self.right = Node(data)
                # se tiver insere o dado na direita
                else:
                    self.right.insert(data)
        else:
            self.data = Node(data)

    def insertAll(self, array):
        arraySize = len(array)
        if arraySize > 0:
            for data in array:
                self.insert(data)
        else:
            print("Array vazio")
    
    def printTreeRaiz(self):
        print(self.data)

    def printTree(self):
        print(self.data)
        
        if self.left:
            self.left.printTree()
        
        if self.right:
            self.right.printTree()

    def search(self, number):
        if self.data == number:
            print("Nó encontrado: ", number)
            
        if self.left:
            self.left.search(number)
        
        if self.right:
            self.right.search(number)
        
        
binaryTree = Node(10)

# binaryTree.insert(5)
# binaryTree.insert(1)
# binaryTree.insert(2)
# binaryTree.insert(3)
# binaryTree.insert(6)
# binaryTree.insert(15)
# binaryTree.insert(12)
# binaryTree.insert(16)

binaryTree.insertAll([9, 2, 6, 3, 11, 40, 20, 50, 1])
binaryTree.printTree()

binaryTree.search(20)