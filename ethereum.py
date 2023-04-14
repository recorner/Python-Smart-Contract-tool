from web3 import Web3, HTTPProvider
from solcx import compile_source, compile_files
import json

# Connect to an Ethereum node
w3 = Web3(HTTPProvider('https://mainnet.infura.io/v3/your_project_id'))

# Compile the smart contract
contract_source = """
pragma solidity ^0.8.0;

contract HelloWorld {
    string message;

    constructor(string memory _message) {
        message = _message;
    }

    function getMessage() public view returns (string memory) {
        return message;
    }

    function setMessage(string memory _message) public {
        message = _message;
    }
}
"""
compiled_contract = compile_source(contract_source)

# Deploy the smart contract
abi = compiled_contract['<stdin>:HelloWorld']['abi']
bytecode = compiled_contract['<stdin>:HelloWorld']['bin']
contract = w3.eth.contract(abi=abi, bytecode=bytecode)

tx_hash = contract.constructor('Hello, World!').transact()
tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)

contract_address = tx_receipt.contractAddress
print(f"Contract deployed at address: {contract_address}")

# Interact with the smart contract
contract_instance = w3.eth.contract(address=contract_address, abi=abi)

message = contract_instance.functions.getMessage().call()
print(f"Current message: {message}")

contract_instance.functions.setMessage('Hello, Etherium!').transact()

message = contract_instance.functions.getMessage().call()
print(f"Updated message: {message}")
