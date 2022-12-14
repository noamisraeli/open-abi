# This file is generated using the Etheruem API generator.
# the file contains the basic functions for interacting with ethereum contract.
import pydantic

import typing

from openabi.python.contract_client import ContractClient


class ECR20Client(ContractClient):
	ABI = """[
    {
        "constant": true,
        "inputs": [],
        "name": "name",
        "outputs": [
            {
                "name": "",
                "type": "string"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": false,
        "inputs": [
            {
                "name": "_spender",
                "type": "address"
            },
            {
                "name": "_value",
                "type": "uint256"
            }
        ],
        "name": "approve",
        "outputs": [
            {
                "name": "",
                "type": "bool"
            }
        ],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [],
        "name": "totalSupply",
        "outputs": [
            {
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": false,
        "inputs": [
            {
                "name": "_from",
                "type": "address"
            },
            {
                "name": "_to",
                "type": "address"
            },
            {
                "name": "_value",
                "type": "uint256"
            }
        ],
        "name": "transferFrom",
        "outputs": [
            {
                "name": "",
                "type": "bool"
            }
        ],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [],
        "name": "decimals",
        "outputs": [
            {
                "name": "",
                "type": "uint8"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [
            {
                "name": "_owner",
                "type": "address"
            }
        ],
        "name": "balanceOf",
        "outputs": [
            {
                "name": "balance",
                "type": "uint256"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [],
        "name": "symbol",
        "outputs": [
            {
                "name": "",
                "type": "string"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": false,
        "inputs": [
            {
                "name": "_to",
                "type": "address"
            },
            {
                "name": "_value",
                "type": "uint256"
            }
        ],
        "name": "transfer",
        "outputs": [
            {
                "name": "",
                "type": "bool"
            }
        ],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [
            {
                "name": "_owner",
                "type": "address"
            },
            {
                "name": "_spender",
                "type": "address"
            }
        ],
        "name": "allowance",
        "outputs": [
            {
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "payable": true,
        "stateMutability": "payable",
        "type": "fallback"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "name": "owner",
                "type": "address"
            },
            {
                "indexed": true,
                "name": "spender",
                "type": "address"
            },
            {
                "indexed": false,
                "name": "value",
                "type": "uint256"
            }
        ],
        "name": "Approval",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "name": "from",
                "type": "address"
            },
            {
                "indexed": true,
                "name": "to",
                "type": "address"
            },
            {
                "indexed": false,
                "name": "value",
                "type": "uint256"
            }
        ],
        "name": "Transfer",
        "type": "event"
    }
]"""
	def name(self) -> str:
		function_abi_signature = 'name()'
		result = self.api.make_call(self._address, function_abi_signature, [])

		return result
	def approve(self, _spender: pydantic.constr(regex=r'^0x[0-9a-fA-F]{40}$'), _value: int) -> bool:
		function_abi_signature = 'approve(address,uint256)'
		result = self.api.make_call(self._address, function_abi_signature, [_spender, _value])

		return result
	def total_supply(self) -> int:
		function_abi_signature = 'totalSupply()'
		result = self.api.make_call(self._address, function_abi_signature, [])

		return result
	def transfer_from(self, _from: pydantic.constr(regex=r'^0x[0-9a-fA-F]{40}$'), _to: pydantic.constr(regex=r'^0x[0-9a-fA-F]{40}$'), _value: int) -> bool:
		function_abi_signature = 'transferFrom(address,address,uint256)'
		result = self.api.make_call(self._address, function_abi_signature, [_from, _to, _value])

		return result
	def decimals(self) -> int:
		function_abi_signature = 'decimals()'
		result = self.api.make_call(self._address, function_abi_signature, [])

		return result
	class balanceOf_output(pydantic.BaseModel):
		balance: int
	def balance_of(self, _owner: pydantic.constr(regex=r'^0x[0-9a-fA-F]{40}$')) -> balanceOf_output:
		function_abi_signature = 'balanceOf(address)'
		result = self.api.make_call(self._address, function_abi_signature, [_owner])

		return self.balanceOf_output(result)
	def symbol(self) -> str:
		function_abi_signature = 'symbol()'
		result = self.api.make_call(self._address, function_abi_signature, [])

		return result
	def transfer(self, _to: pydantic.constr(regex=r'^0x[0-9a-fA-F]{40}$'), _value: int) -> bool:
		function_abi_signature = 'transfer(address,uint256)'
		result = self.api.make_call(self._address, function_abi_signature, [_to, _value])

		return result
	def allowance(self, _owner: pydantic.constr(regex=r'^0x[0-9a-fA-F]{40}$'), _spender: pydantic.constr(regex=r'^0x[0-9a-fA-F]{40}$')) -> int:
		function_abi_signature = 'allowance(address,address)'
		result = self.api.make_call(self._address, function_abi_signature, [_owner, _spender])

		return result
