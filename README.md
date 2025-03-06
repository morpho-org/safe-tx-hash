# Safe tx hash

Script to compute a [safe tx hash](https://help.safe.global/en/articles/40814-what-is-the-safe-transaction-hash-safetxhash).

## Setup

1. `python3 -m venv ./venv`
2. `source venv/bin/activate`
3. `pip install -r requirements.txt`

## Use

1. Fill `./safe-tx.json` (following the example of [this tx](https://app.safe.global/transactions/tx?safe=base:0xcBa28b38103307Ec8dA98377ffF9816C164f9AFa&id=multisig_0xcBa28b38103307Ec8dA98377ffF9816C164f9AFa_0x1bf99e3cf2d2272960c8a02ca4163459ad240de7995bec237a886b84968a077c) in [`./safe-tx.json`](./safe-tx.json))
2. Run `python3 main.py`

## Dependencies

- [eth-hash](https://pypi.org/project/eth-hash/) for hashing
- [eth-abi](https://pypi.org/project/eth-abi/) for encoding
