import typing

from eth_abi import encode, decode
import pydantic
import web3
from web3.contract import Contract

Bytes32 = bytes
Address = pydantic.constr(regex=r'^0x[0-9a-fA-F]{40}$')


class ContractClient:
    ABI: str 

    def __init__(self, address: Address, w3_provider: web3.Web3) -> None:
        assert self.ABI
        self._address = address
        self._web3_provider = w3_provider
        self._contract_api: typing.Optional[Contract] = None
    
    def init(self):
        self._contract_api = self._web3_provider.eth.contract(self._address, abi=self.ABI)
    
    def make_call(self, function_signature: str, arguments: typing.List):
        data = encode(function_signature, args=arguments)
        output = self._web3_provider.eth.call({
            'to': self._address,
            'data': data
        })
        return decode(function_signature, output)
        

    

    