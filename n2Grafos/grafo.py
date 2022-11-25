import matplotlib.pyplot as plt 
import networkx as nx

# inicializando o grafo
G = nx.Graph()

# adicionando vertices
G.add_node("SC")
G.add_node("RS")
G.add_node("PR")
G.add_node("SP")
G.add_node("RJ")
G.add_node("MG")
G.add_node("ES")
G.add_node("DF")
G.add_node("MT")
G.add_node("PA")
G.add_node("RR")
G.add_node("AM")
G.add_node("TO")
G.add_node("AP")
G.add_node("CE")
G.add_node("PI")
G.add_node("BA")
G.add_node("AC")
G.add_node("RO")
G.add_node("GO")

numVertices = str(G.number_of_nodes())


# adicionando arestas
# RS
G.add_edge("RS", "SC", weight=2)

# SC
G.add_edge("SC", "RS", weight=2)
G.add_edge("SC", "PR", weight=2)

# PR
G.add_edge("PR", "SC", weight=2)
G.add_edge("PR", "SP", weight=1)

# SP
G.add_edge("SP", "PR", weight=1)
G.add_edge("SP", "RJ", weight=4)
G.add_edge("SP", "MG", weight=3)
G.add_edge("SP", "MT", weight=6)

# RJ
G.add_edge("RJ", "SP", weight=4)
G.add_edge("RJ", "ES", weight=1)

# MG
G.add_edge("MG", "SP", weight=3)
G.add_edge("MG", "ES", weight=3)
G.add_edge("MG", "DF", weight=2)

# ES
G.add_edge("ES", "RJ", weight=1)
G.add_edge("ES", "MG", weight=3)

# DF
G.add_edge("DF", "MG", weight=2)

# MT
G.add_edge("MT", "SP", weight=6)
G.add_edge("MT", "PA", weight=6)

# PA
G.add_edge("PA", "MT", weight=6)
G.add_edge("PA", "RR", weight=5)

# RR
G.add_edge("RR", "PA", weight=5)
G.add_edge("RR", "AM", weight=4)

# AM
G.add_edge("AM", "RR", weight=4)
G.add_edge("AM", "TO", weight=8)

# TO
G.add_edge("TO", "AM", weight=8)
G.add_edge("TO", "AP", weight=6)

# AP
G.add_edge("AP", "TO", weight=6)
G.add_edge("AP", "CE", weight=6)

# CE
G.add_edge("CE", "AP", weight=6)
G.add_edge("CE", "PI", weight=3)

# PI
G.add_edge("PI", "CE", weight=3)
G.add_edge("PI", "BA", weight=2)

# BA
G.add_edge("BA", "PI", weight=2)
G.add_edge("BA", "AC", weight=12)

# AC
G.add_edge("AC", "BA", weight=12)
G.add_edge("AC", "RO", weight=3)

# RO
G.add_edge("RO", "AC", weight=3)
G.add_edge("RO", "GO", weight=6)

# GO
G.add_edge("GO", "RO", weight=6)

numArestas = str(G.number_of_edges())

# prints
print("\nNúmero de Vértices do grafo: " + numVertices)
# print("Número de Arestas do grafo: " + numArestas)

pesoArestas = {
  # RS
  "RS-SC" : ["2"],
  
  # SC
  "SC-PR" : ["2"],
  
  # PR
  "PR-SP" : ["1"],
  
  # SP
  "SP-RJ" : ["4"],
  "SP-MG" : ["3"],
  "SP-MT" : ["6"],

  # RJ
  "RJ-ES" : ["1"],

  # MG 
  "MG-ES" : ["3"],
  "MG-DF" : ["2"],

  # MT
  "MT-PA" : ["6"],

  # PA
  "PA-RR" : ["5"],

  # RR
  "RR-AM" : ["4"],

  # AM
  "AM-TO" : ["8"],

  # TO
  "TO-AP" : ["6"],

  # AP
  "AP-CE" : ["6"],

  # CE
  "CE-PI" : ["3"],

  # PI
  "PI-BA" : ["2"],

  # BA
  "BA-AC": ["12"],
  
  # AC
  "AC-RO" : ["3"],
  
  # RO
  "RO-GO" : ["6"]
}

print("\nPeso das arestas:")
for i in pesoArestas:
  print(i, pesoArestas[i])
