import matplotlib.pyplot as plt 
import networkx as nx

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

numVertices = G.number_of_nodes()

pesoArestas = {
  "RS-SC" : ["1"],
  "SC" : ["2"],
  "PR" : ["2"],
  "SP" : ["4"],
  "RJ" : ["2"],
  "MG" : ["3"],
  "ES" : ["2"],
  "DF" : ["1"],
  "MT" : ["2"],
  "PA" : ["2"],
  "RR" : ["2"],
  "AM" : ["2"],
  "TO" : ["2"],
  "AP" : ["2"],
  "CE" : ["2"],
  "PI" : ["2"],
  "BA" : ["2"],
  "AC" : ["2"],
  "RO" : ["2"],
  "GO" : ["2"]
}



# print('vertices: ', n_vertices)
# nx.draw(G, with_labels=True)
# plt.show()