# blockchain_interaction.py

from web3 import Web3

class BlockchainInteraction:
    def __init__(self, contract_address, contract_abi):
        self.w3 = Web3(Web3.HTTPProvider("https://rinkeby.infura.io/v3/your_project_id"))
        self.contract_address = contract_address
        self.contract_abi = contract_abi
        self.contract = self.w3.eth.contract(address=self.contract_address, abi=self.contract_abi)

    def verify_component(self, component_id):
        authenticity = self.contract.functions.verifyComponent(component_id).call()
        print("Autenticidad del componente:", "Auténtico" if authenticity else "Falso")
