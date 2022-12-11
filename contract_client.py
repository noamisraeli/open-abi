import typing

import pydantic
import web3
from web3.contract import Contract

from eth_abi import (
    decode
)

UInt256 = int
Bytes32 = bytes
Address = pydantic.constr(regex=r'^0x[0-9a-fA-F]{40}$')


def parse_function_return_value(function_return_value, contract, function_signature):
    # Decode the return value using the ABI and function signature
    decoded = contract.decode_abi(function_signature, function_return_value)

    # Return the decoded value
    return decoded

# Parse the return value using the contract ABI and function signature
def parse_function_return_value(function_return_value, contract_abi, function_signature):
    # Find the function in the ABI by its signature
    function = next(filter(lambda x: x['signature'] == function_signature, contract_abi), None)

    # Decode the return value using the ABI and function signature
    decoded = decode_single(function['outputs'], function_return_value)

    # Return the decoded value
    return decoded

class ContractClient:
    ABI: str 

    def __init__(self, address: Address, w3_provider: web3.Web3) -> None:
        assert self.ABI
        self._address = address
        self._web3_provider = w3_provider
        self._contract_api: typing.Optional[Contract] = None
    
    def init(self):
        self._contract_api = self._web3_provider.eth.contract(self._address, abi=self.ABI)
    

    

    