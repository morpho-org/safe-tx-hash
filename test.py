from main import compute_safe_tx_hash

def test_safe_tx_hash():
    test_tx = {
        "to": "0xBAa5CC21fd487B8Fcc2F632f3F4E8D37262a0842",
        "value": 0,
        "data": "0xa9059cbb000000000000000000000000f057afeec22e220f47ad4220871364e9e828b2e900000000000000000000000000000000000000000001a784379d99db42000000",
        "operation": 0,
        "safeTxGas": 0,
        "baseGas": 0,
        "gasPrice": 0,
        "gasToken": "0x0000000000000000000000000000000000000000",
        "refundReceiver": "0x0000000000000000000000000000000000000000",
        "nonce": 11,
        "safe": "0xcBa28b38103307Ec8dA98377ffF9816C164f9AFa",
        "chainId": 8453
    }
    
    expected_hash = "0x1bf99e3cf2d2272960c8a02ca4163459ad240de7995bec237a886b84968a077c"
    computed_hash = compute_safe_tx_hash(test_tx)
    assert computed_hash == expected_hash

if __name__ == "__main__":
    test_safe_tx_hash()
    print("All tests passed!") 
