# Imagen de Curso Principiante a Intermedio CryptoZombies
En primer lugar se adjunta una imagen mostrando como el curso Principiante a Intermediario en Solidity ha sido completado.

# Smart Contract de Control de Acceso con Árbol de Merkle

## Descripción

Este **Smart Contract de Solidity** (`AccessControlMerkle.sol`) funciona como el punto de inicio de una cadena de verificación usando el **Árbol de Merkle** (Merkle Tree).

Se utiliza para implementar un mecanismo de **control de acceso privado** donde solo se almacena la **Raíz de Merkle** (el hash principal de una lista de acceso), permitiendo a los usuarios demostrar su inclusión en esa lista sin revelar los datos de todos los demás. Este método es crucial para **ahorrar costes de gas** en la Blockchain. 

## Conceptos Clave en Solidity

| Concepto | Rol en el Contrato |
| :--- | :--- |
| **Raíz de Merkle** | El único hash (`bytes32`) almacenado públicamente. Representa toda la lista privada. |
| **Hoja (Leaf)** | El hash de la dirección del usuario (`msg.sender`) que busca acceso. |
| **Prueba (Proof)** | La lista de hashes intermedios que el usuario proporciona para validar su pertenencia. |
| **`MerkleProof.verify`** | Función de la librería de OpenZeppelin que realiza el cálculo de verificación en la cadena. |

## Pre-requisitos

1.  Un entorno de desarrollo para Solidity (como **Hardhat** o **Truffle**).
2.  La librería de **OpenZeppelin Contracts** instalada (`npm install @openzeppelin/contracts`), ya que el contrato la importa.

## 1. `AccessControlMerkle.sol` (Código del Contrato)

(Nota: El código del contrato se inserta aquí)

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importar la librería de OpenZeppelin para la verificación Merkle
import "@openzeppelin/contracts/utils/cryptography/MerkleProof.sol";

contract AccessControlMerkle {
    bytes32 public merkleRoot;
    mapping(address => bool) private hasClaimed;

    constructor(bytes32 _merkleRoot) {
        merkleRoot = _merkleRoot;
    }

    function verifyAccess(bytes32[] calldata proof, bytes32 leaf) public {
        bool isValid = MerkleProof.verify(proof, merkleRoot, leaf);

        require(isValid, "MerkleProof: La prueba no es valida o el usuario no esta en la lista.");
        require(!hasClaimed[msg.sender], "AccessControl: Este usuario ya ha reclamado su acceso.");

        hasClaimed[msg.sender] = true;
        
        emit AccessGranted(msg.sender);
    }

    event AccessGranted(address indexed user);
}

## 2. Notas de Ejecución y Flujo de Trabajo

El Smart Contract no se puede ejecutar directamente en la terminal. Sigue este flujo de trabajo para usar la verificación Merkle:

1.  Cálculo Off-chain (Administrador): El administrador de la lista privada debe escribir un script (usando Node.js, Python, etc.) para:
	- Generar una lista de direcciones permitidas.
	- Calcular el hash de cada dirección (el Leaf).
	- Calcular la Raíz de Merkle a partir de todos los Leaves.

2.  Despliegue (Administrador): El contrato se despliega en la red blockchain, pasando la Raíz de Merkle calculada al constructor.

3.  Distribución Off-chain (Administrador): El administrador proporciona a cada usuario autorizado su Prueba (Proof) personal, que es necesaria para interactuar con el contrato.

4.  Llamada On-chain (Usuario): El usuario llama a la función verifyAccess(proof, leaf) en el Smart Contract. Si la proof es correcta y coincide con la merkleRoot almacenada, el acceso es concedido.
