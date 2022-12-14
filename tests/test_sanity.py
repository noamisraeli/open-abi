from openabi.generator import generate
from web3 import Web3
from web3.middleware import geth_poa_middleware 

if __name__ == '__main__':
    contract_name = 'ECR20'

    with open(f'tests/examples/{contract_name}.json', 'r') as f:
        contract_abi_string = f.read()
    
    generate(contract_name=contract_name, contract_abi_string=contract_abi_string, output_dir='tests/generated')
    
    from tests.generated.api import ECR20Client
    from openabi.python.contract_client import EtheruemGatewayAPI

    API_KEY = "7e135dbc63904c30808f84ff52a92343"

    BASE_URL = f"https://mainnet.infura.io/v3/{API_KEY}"

    w3_provider = Web3.HTTPProvider(BASE_URL)
    w3 = Web3(w3_provider)

    w3.middleware_onion.inject(geth_poa_middleware, layer=0)

    etheruem_gateway = EtheruemGatewayAPI(w3)

    user_account = '0x68b3465833fb72A70ecDF485E0e4C7bD8665Fc45'

    contract_account = '0xc3761EB917CD790B30dAD99f6Cc5b4Ff93C4F9eA'

    client = ECR20Client(address=contract_account, gateway_api=etheruem_gateway)

    client.init()
    balance = client.balance_of('0x68b3465833fb72A70ecDF485E0e4C7bD8665Fc45')
    print(balance['balance'])