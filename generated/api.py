# This file is generated using the Etheruem API generator.
# the file contains the basic functions for interacting with ethereum contract.
import pydantic

import typing

from contract_client import ContractClient


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
		result = self._contract_api.functions.name().call()

		return result

	def approve(self, _spender: pydantic.constr(regex=r'^0x[0-9a-fA-F]{40}$'), _value: int) -> bool:
		result = self._contract_api.functions.approve(_spender, _value).call()

		return result

	def total_supply(self) -> int:
		result = self._contract_api.functions.totalSupply().call()

		return result

	def transfer_from(self, _from: pydantic.constr(regex=r'^0x[0-9a-fA-F]{40}$'), _to: pydantic.constr(regex=r'^0x[0-9a-fA-F]{40}$'), _value: int) -> bool:
		result = self._contract_api.functions.transferFrom(_from, _to, _value).call()

		return result

	def decimals(self) -> int:
		result = self._contract_api.functions.decimals().call()

		return result

	balanceOf_output = typing.TypedDict("balanceOf_output", balance=int)
	def balance_of(self, _owner: pydantic.constr(regex=r'^0x[0-9a-fA-F]{40}$')) -> balanceOf_output:
		result = self._contract_api.functions.balanceOf(_owner).call()

		return result

	def symbol(self) -> str:
		result = self._contract_api.functions.symbol().call()

		return result

	def transfer(self, _to: pydantic.constr(regex=r'^0x[0-9a-fA-F]{40}$'), _value: int) -> bool:
		result = self._contract_api.functions.transfer(_to, _value).call()

		return result

	def allowance(self, _owner: pydantic.constr(regex=r'^0x[0-9a-fA-F]{40}$'), _spender: pydantic.constr(regex=r'^0x[0-9a-fA-F]{40}$')) -> int:
		result = self._contract_api.functions.allowance(_owner, _spender).call()

		return result

