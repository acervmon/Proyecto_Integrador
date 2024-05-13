// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SupplyChain {
    struct Component {
        string componentId;
        bool isAuthentic;
    }

    mapping(string => Component) public components;

    event ComponentVerified(string indexed componentId, bool isAuthentic);

    function addComponent(string memory _componentId) public {
        // Asumiendo que el componente se agrega por el proveedor
        require(components[_componentId].componentId == "", "Component already exists");
        components[_componentId] = Component(_componentId, false);
    }

    function verifyComponent(string memory _componentId) public {
        // Asumiendo que la verificación del componente se realiza por el fabricante o cualquier otro participante
        require(components[_componentId].componentId != "", "Component does not exist");
        components[_componentId].isAuthentic = true;
        emit ComponentVerified(_componentId, true);
    }
}
