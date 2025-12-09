// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importar la librería MerkleProof de OpenZeppelin.
// Esta librería es esencial para verificar las pruebas (proofs) en la cadena.
import "@openzeppelin/contracts/utils/cryptography/MerkleProof.sol";

contract AccessControlMerkle {
    // La variable que almacena el hash principal, la Raíz de Merkle (Merkle Root).
    bytes32 public merkleRoot;

    // Mapeo para registrar si una dirección ya ha reclamado su acceso (para evitar doble uso).
    mapping(address => bool) private hasClaimed;

    /**
     * @dev Constructor: Se ejecuta solo una vez al desplegar el contrato.
     * @param _merkleRoot La raíz de Merkle calculada fuera de la cadena (off-chain).
     */
    constructor(bytes32 _merkleRoot) {
        merkleRoot = _merkleRoot;
    }

    /**
     * @notice Función principal de acceso privado.
     * Permite a un usuario demostrar que está incluido en la lista privada.
     * @param proof El camino (path) de hashes necesario para llegar desde el dato del usuario
     * hasta la Raíz de Merkle.
     * @param leaf El 'dato' del usuario (el hash de su dirección).
     */
    function verifyAccess(bytes32[] calldata proof, bytes32 leaf) public {
        // 1. Verificar la Raíz de Merkle
        // MerkleProof.verify comprueba que el 'leaf' (usuario) está conectado a la 'merkleRoot'
        // a través de los hashes intermedios ('proof').
        bool isValid = MerkleProof.verify(proof, merkleRoot, leaf);

        require(isValid, "MerkleProof: La prueba no es valida o el usuario no esta en la lista.");

        // 2. Verificar que no haya sido reclamado previamente
        require(!hasClaimed[msg.sender], "AccessControl: Este usuario ya ha reclamado su acceso.");

        // 3. Otorgar Acceso y Registrar el Reclamo
        hasClaimed[msg.sender] = true;

        // Aquí iría la lógica de negocio real (ejecutar una transacción, mintear un token, etc.)
        emit AccessGranted(msg.sender);
    }

    // Evento para notificar que alguien ha obtenido acceso.
    event AccessGranted(address indexed user);
}
