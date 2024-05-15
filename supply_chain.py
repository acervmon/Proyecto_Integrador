# supply_chain
import networkx as nx
import matplotlib.pyplot as plt

class SupplyChainGraph:
    def __init__(self):
        self.G = nx.DiGraph()
        self.nodes = ["Proveedor", "Fabricante", "Distribuidor", "Minorista", "Consumidor"]
        self.edges = [("Proveedor", "Fabricante"), ("Fabricante", "Distribuidor"),
        ("Distribuidor", "Minorista"), ("Minorista", "Consumidor")]

    def create_graph(self):
        self.G.add_nodes_from(self.nodes)
        self.G.add_edges_from(self.edges)

    def draw_graph(self):
        pos = nx.spring_layout(self.G)
        nx.draw(self.G, pos, with_labels=True, node_color='skyblue', node_size=4000, edge_color='k', linewidths=1, font_size=15)
        plt.show()

class Node:
    def __init__(self, name):
        self.name = name
        self.data = []

    def add_data(self, data, nodes):
        print(f"{self.name} agregando datos: {data}")
        self.data.append(data)
        self.broadcast_data(data, nodes)

    def broadcast_data(self, data, nodes):
        # En un entorno real, aquí se aplicarían mecanismos de validación antes de aceptar los datos
        print(f"{self.name} transmite datos: {data}")
        for node in nodes:
            if node != self:
                node.receive_data(data)

    def receive_data(self, data):
        print(f"{self.name} recibió datos: {data}")
        self.data.append(data)

