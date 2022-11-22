class Grafo:

    # construtor
    def __init__(self, node):
        # inicializa os vértices
        self.node = node
        
        # a primeira lista terá o tamanho = número de vértices, recebendo em todas as posições 0
        # e vai construir X linhas, que recebe novamente o número de vértices
        # assim criando uma matriz n por n, sendo n = número de vértices
        self.matriz = [[0]*self.node for node in range(self.node)]

    def addEdge(self, node1, node2):
        
        # por não termos "vértice 0", temos que diminuir 1, pois o python começa a contar a lista pelo 0
        # exemplo: podermos ter um vértice 2, porém não termos a posição 2 na lista, por começar por 0 seria [0, 1]
        self.matriz[node1 - 1][node2 - 1] = 1

    def showMatriz(self):
        print('A matriz de adjacência é:')
        # loop pra percorrer todas as listas
        for i in range(self.node):
            print(self.matriz[i])


# passamos o número de vértices como parâmetro
m = Grafo(20)

# adicionamos as arestas

# RS = 1
m.addEdge(1, 2)

# SC = 2
m.addEdge(2, 1)
m.addEdge(2, 3)

# PR = 3
m.addEdge(3, 2)
m.addEdge(3, 4)

# SP = 4
m.addEdge(4, 3)
m.addEdge(4, 5)
m.addEdge(4, 6)
m.addEdge(4, 9)

# RJ = 5
m.addEdge(5, 4)
m.addEdge(5, 7)

# MG = 6
m.addEdge(6, 4)
m.addEdge(6, 7)
m.addEdge(6, 8)

# ES = 7
m.addEdge(7, 5)
m.addEdge(7, 6)

# DF = 8
m.addEdge(8, 6)

# MT = 9
m.addEdge(9, 4)
m.addEdge(9, 10)

# PA = 10
m.addEdge(10, 9)
m.addEdge(10, 11)

# RR = 11
m.addEdge(11, 10)
m.addEdge(11, 12)

# AM = 12
m.addEdge(12, 11)
m.addEdge(12, 13)

# TO = 13
m.addEdge(13, 12)
m.addEdge(13, 14)

# AP = 14
m.addEdge(14, 13)
m.addEdge(14, 15)

# CE = 15
m.addEdge(15, 14)
m.addEdge(15, 16)

# PI = 16
m.addEdge(16, 15)
m.addEdge(16, 17)

# BA = 17
m.addEdge(17, 16)
m.addEdge(17, 18)

# AC = 18
m.addEdge(18, 17)
m.addEdge(18, 19)

# RO = 19
m.addEdge(19, 18)
m.addEdge(19, 20)

# GO = 20
m.addEdge(20, 19)


# mostrar a matriz
m.showMatriz()
