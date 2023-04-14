# Python Smart Contract DEployment tool on web3

# Blockchain CLI Tool

A Python-based CLI tool for deploying and managing smart contracts on various blockchain platforms like Ethereum, Binance Smart Chain, and Polygon.

This tool streamlines the deployment process and makes it easier for developers to test and manage their contracts.

## Requirements

- Python 3.x
- `click`
- `eth-account`
- `eth-brownie`
- `eth-utils`
- `web3`

## Installation

1. Clone the repository
https://github.com/recorner/Python-Smart-Contract-tool.git


2. Install the required packages
pip install -r requirements.txt


## Usage

### Deploy a smart contract
python cli.py deploy <network> <contract_name> <private_key> [args...]


Example:
python cli.py deploy ethereum my_contract_file 0x1234...5678 arg1 arg2 arg3


### Get the address of a deployed contract

python cli.py get_balance <network> <address>


Example:
python cli.py get_balance polygon_mumbai 0x1234...5678


## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/my-new-feature`)
5. Create a new Pull Request

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


