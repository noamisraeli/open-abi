from generated.api import ECR20Client
from web3 import Web3
from web3.middleware import geth_poa_middleware 

if __name__ == '__main__':
    API_KEY = "7e135dbc63904c30808f84ff52a92343"

    BASE_URL = f"https://mainnet.infura.io/v3/{API_KEY}"

    w3_provider = Web3.HTTPProvider(BASE_URL)
    w3 = Web3(w3_provider)
    w3.middleware_onion.inject(geth_poa_middleware, layer=0)

    user_account = '0x68b3465833fb72A70ecDF485E0e4C7bD8665Fc45'

    contract_account = '0xc3761EB917CD790B30dAD99f6Cc5b4Ff93C4F9eA'

    client = ECR20Client(address=contract_account, w3_provider=w3)
    client.init()
    balance = client.balance_of('0x68b3465833fb72A70ecDF485E0e4C7bD8665Fc45')
    print(balance['balance'])