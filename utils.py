import click

def validate_address(ctx, param, value):
    """
    Validate Ethereum address format.
    """
    if value is not None:
        if not Web3.isAddress(value):
            raise click.BadParameter('Invalid address format.')
    return value

def validate_private_key(ctx, param, value):
    """
    Validate Ethereum private key format.
    """
    if value is not None:
        if not Web3.isHex(value):
            raise click.BadParameter('Invalid private key format.')
        if len(value) != 66 or value[:2] != '0x':
            raise click.BadParameter('Invalid private key length or prefix.')
    return value

def validate_contract_address(ctx, param, value):
    """
    Validate Ethereum contract address format.
    """
    if value is not None:
        if not Web3.isChecksumAddress(value):
            raise click.BadParameter('Invalid contract address format.')
    return value

def get_gas_price(network):
    """
    Get the current gas price for the specified network.
    """
    if network == 'mainnet':
        return w3.eth.gas_price
    elif network == 'rinkeby':
        return w3.eth.gas_price('rinkeby')
    else:
        raise ValueError('Invalid network specified.')

def get_gas_limit():
    """
    Get the default gas limit for contract transactions.
    """
    return 200000

def get_account(private_key):
    """
    Get an account object from the specified private key.
    """
    return w3.eth.account.privateKeyToAccount(private_key)

def get_contract_interface(contract_name):
    """
    Get the ABI and bytecode for the specified contract.
    """
    with open(f'contracts/{contract_name}.json') as f:
        contract_data = json.load(f)
    return contract_data['abi'], contract_data['bytecode']

def load_contract_instance(contract_name, contract_address):
    """
    Load a contract instance with the specified ABI and address.
    """
    abi, bytecode = get_contract_interface(contract_name)
    return w3.eth.contract(abi=abi, address=contract_address)
