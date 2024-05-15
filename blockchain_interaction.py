import json
from web3 import Web3

# blockchain_interaction.py
class BlockchainInteraction:
    """
    This class interacts with a blockchain contract.
    """

    def __init__(self, contract_address, contract_abi):
        self.w3 = Web3(Web3.HTTPProvider("https://rinkeby.infura.io/v3/your_project_id"))
        self.contract_address = contract_address
        self.contract_abi = contract_abi
        self.contract = self.w3.eth.contract(address=self.contract_address, abi=self.contract_abi)

    def verify_component(self, component_id):
        """
        Verifies the authenticity of a component.
        """
        authenticity = self.contract.functions.verifyComponent(component_id).call()
        print("Autenticidad del componente:", "Auténtico" if authenticity else "Falso")

    def is_connected(self):
        """
        Checks if the blockchain connection is active.
        """
        return self.w3.isConnected()

# Verificar la conexión
blockchain_interaction = BlockchainInteraction("0xYourContractAddress", json.loads('YourContractABI'))
print("Conectado:", blockchain_interaction.is_connected())

# Interactuar con el contrato
# Supongamos que hay una función para verificar la autenticidad de un componente
COMPONENT_ID = "C1234"
authenticity = blockchain_interaction.contract.functions.verifyComponent(COMPONENT_ID).call()
print("Autenticidad del componente:", "Auténtico" if authenticity else "Falso")

# Pruebas y Validación

def test_verify_component():
    """
    Tests the verify_component method.
    """
    # Asumiendo que la función anterior está definida y `contract` es accesible
    component_id = "C1234"
    expected = True  # Asumimos que esperamos un resultado verdadero para la prueba
    assert blockchain_interaction.contract.functions.verifyComponent(component_id).call() == expected, "La verificación del componente falló"
