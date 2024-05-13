# main.py

from supply_chain import SupplyChainGraph, Node
from blockchain_interaction import BlockchainInteraction

def main():
    # Crear y dibujar el gráfico de la cadena de suministro
    supply_chain_graph = SupplyChainGraph()
    supply_chain_graph.create_graph()
    supply_chain_graph.draw_graph()

    # Crear nodos
    nodes = [Node("Nodo1"), Node("Nodo2"), Node("Nodo3")]

    # Agregar y transmitir datos
    nodes[0].add_data("Componente A1")

    # Interactuar con la blockchain
    contract_address = "0xYourContractAddress"
    contract_abi = json.loads('YourContractABI')
    blockchain_interaction = BlockchainInteraction(contract_address, contract_abi)
    component_id = "C1234"
    blockchain_interaction.verify_component(component_id)

if __name__ == "__main__":
    main()