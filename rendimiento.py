import networkx as nx
import matplotlib.pyplot as plt

# Crear un grafo dirigido para representar la cadena de suministro
G = nx.DiGraph()

# Agregar nodos con roles en la cadena de suministro
nodes = ["Proveedor", "Fabricante", "Distribuidor", "Minorista", "Consumidor"]
G.add_nodes_from(nodes)

# Conectar los nodos para mostrar el flujo de la cadena de suministro
edges = [("Proveedor", "Fabricante"), ("Fabricante", "Distribuidor"),
    ("Distribuidor", "Minorista"), ("Minorista", "Consumidor")]
G.add_edges_from(edges)

# Dibujar el grafo
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=4000, edge_color='k', linewidths=1, font_size=15)
plt.show()
