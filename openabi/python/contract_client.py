import typing
import re 

from eth_abi import encode, decode
import pydantic
import web3

Address = pydantic.constr(regex=r'^0x[0-9a-fA-F]{40}$')

class EtheruemGatewayAPI:
    def __init__(self, w3: web3.Web3) -> None:
        self._web3_provider = w3

    def _encode_input_data(self, function_signature: str, arguments: typing.List):
        signature = self._web3_provider.keccak(text=function_signature).hex()[:8]
        types = re.search(r"\((\w+)\)", function_signature).group(0).split(",")
        return signature + encode(types, arguments)

    def make_call(self, address: Address, function_signature: str, arguments: typing.List) -> typing.Any:
        data = self._encode_input_data(function_signature, arguments)

        output = self._web3_provider.eth.call({
            'to': address,
            'data': data
        })
        return decode(function_signature, output)


TGatewayAPI = typing.TypeVar('TGatewayAPI')

class ContractClient(typing.Generic[TGatewayAPI]):
    ABI: str 

    def __init__(self, address: Address, gateway_api: TGatewayAPI) -> None:
        assert self.ABI
        self._address = address
        self._gateway_api = gateway_api
    
    def init(self):
        pass

    @property
    def api(self) -> TGatewayAPI:
        return self._gateway_api