import pytest
from click.testing import CliRunner
from web3 import Web3

from cli import deploy_contract, transfer_tokens
from utils import get_gas_price, get_gas_limit, get_account, load_contract_instance


def test_deploy_contract():
    runner = CliRunner()
    result = runner.invoke(deploy_contract, ['--network', 'mainnet', '--private-key', '0x123456789abcdef', '--contract-name', 'MyContract', '--constructor-args', 'arg1,arg2'])
    assert result.exit_code == 0

    # Check if contract address is valid
    assert Web3.isAddress(result.output.strip())

    # Check if contract was deployed successfully
    contract_address = result.output.strip()
    contract_instance = load_contract_instance('MyContract', contract_address)
    assert contract_instance.functions.getArg1().call() == 'arg1'
    assert contract_instance.functions.getArg2().call() == 'arg2'


def test_transfer_tokens():
    runner = CliRunner()
    result = runner.invoke(transfer_tokens, ['--network', 'rinkeby', '--private-key', '0x123456789abcdef', '--token-address', '0x0123456789abcdef', '--to-address', '0xabcdef0123456789', '--amount', '100'])
    assert result.exit_code == 0

    # Check if transaction hash is valid
    assert Web3.isHex(result.output.strip())

    # Check if transaction was successful
    tx_hash = result.output.strip()
    receipt = w3.eth.getTransactionReceipt(tx_hash)
    assert receipt.status == 1


def test_get_gas_price():
    assert isinstance(get_gas_price('mainnet'), int)


def test_get_gas_limit():
    assert isinstance(get_gas_limit(), int)


def test_get_account():
    account = get_account('0x0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef')
    assert isinstance(account, w3.eth.account.Account)


def test_load_contract_instance():
    contract_instance = load_contract_instance('MyContract', '0x0123456789abcdef0123456789abcdef0123456')
    assert contract_instance.functions.getArg1().call() == 'arg1'
    assert contract_instance.functions.getArg2().call() == 'arg2'
