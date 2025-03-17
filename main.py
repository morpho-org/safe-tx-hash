import json
from eth_hash.auto import keccak
from eth_abi import encode

EIP712_PREFIX = bytes.fromhex('1901')
SAFE_TX_TYPEHASH = bytes.fromhex(
    'bb8310d486368db6bd6f849402fdd73ad53d316b5a4b2644ad6efe0f941286d8')
DOMAIN_SEPARATOR_TYPEHASH = bytes.fromhex(
    '47e79534a245952e8b16893a336b85a3d9ea9fa8c573f3d803afb92a79469218')


def compute_safe_tx_hash(tx):
    domain_separator = keccak(encode(
        [
            'bytes32',  # typeHash
            'uint256',  # chainId
            'address'   # safe
        ],
        [
            DOMAIN_SEPARATOR_TYPEHASH,
            tx['chainId'],
            tx['safe']
        ]
    ))

    data_hash = keccak(bytes.fromhex(tx['data'][2:]))

    struct_hash = keccak(encode(
        [
            'bytes32',    # typeHash
            'address',    # to
            'uint256',    # value
            'bytes32',    # data_hash
            'uint8',      # operation
            'uint256',    # safeTxGas
            'uint256',    # baseGas
            'uint256',    # gasPrice
            'address',    # gasToken
            'address',    # refundReceiver
            'uint256',    # nonce
        ],
        [
            SAFE_TX_TYPEHASH,
            tx['to'],
            tx['value'],
            data_hash,
            tx['operation'],
            tx['safeTxGas'],
            tx['baseGas'],
            tx['gasPrice'],
            tx['gasToken'],
            tx['refundReceiver'],
            tx['nonce']
        ]
    ))

    safe_tx_hash = keccak(EIP712_PREFIX + domain_separator + struct_hash)
    return f"0x{safe_tx_hash.hex()}", f"0x{domain_separator.hex()}", f"0x{struct_hash.hex()}"


if __name__ == "__main__":
    with open("safe-tx.json", "rb") as f:
        tx = json.load(f)

    tx_hash, domain_separator, struct_hash = compute_safe_tx_hash(tx)
    print(f"Safe transaction hash:      {tx_hash}")
    print(f"Domain hash:                {domain_separator}")
    print(f"Message hash (struct hash): {struct_hash}")
