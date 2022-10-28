# "networkx" é uma biblioteca python para manipulação de grafos e redes complexas
# https://networkx.org/

# Instalação:
# -> pip install networkx
# import networkx as nx
# Para desenhar os grafos é preciso da biblioteca "matplotlib" + IDE PyCharm


import networkx as nx
import matplotlib.pyplot as plt


# criando um objeto networkx
G = nx.Graph()


# --------- VÉRTICES ---------

# Adicionar vértices
G.add_node()

# Remover vértices
G.remove_node()

# Total de vértices
G.number_of_nodes()

# Visualizar os vértices
print(G.nodes())



# --------- ARESTAS ---------

# Adicionar aresta
G.add_edge(1, 2)

# Remover aresta
G.remove_edge(1, 2)

# Total de Arestas
G.number_of_edges()

# Visualizar as arestas
print(G.edges())



# --------- GRÁFICO ---------

# Desenhar o grafo
nx.draw(G)

# Adicionar rótulos (numeração) aos nós
nx.draw(G, with_labels = True)

# Tamanho dos nós
nx.draw(G, node_size = 1200)

# Cor dos nós
nx.draw(G, node_color = "red")