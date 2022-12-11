import json

from .contract_model import EventAttribute, FunctionAttribute
from .utils import update_each_non_empty_line
from .python_generator import generate_event_models, generate_class_function_implementation

def generate(contract_name: str, contract_abi_string: str):
    # TODO:
    # 1. Use linters for all spaces in between imports and stuff (remove CLASS SEPERATOR)
    # 2. Use padantic.BaseModel instead of typed dict and validate the output of a function with it.
    
    contract_description = json.loads(contract_abi_string)
    contract_events_models = [EventAttribute.parse_obj(i) for i in contract_description if i['type'] == 'event']

    with open('generated/events.py', 'w') as f:
        f.truncate()

        if len(contract_events_models) > 0:
            f.write('import pydantic')

        for i in contract_events_models:
            event_class_string = generate_event_models(i)
            f.write(event_class_string)
        
        f.write('\n') # end of file space

    contract_function_models = [FunctionAttribute.parse_obj(i) for i in contract_description if i['type'] == 'function']
    
    with open('generated/api.py', 'w') as f:
        f.truncate()
        
        f.write('# This file is generated using the Etheruem API generator.\n# the file contains the basic functions for interacting with ethereum contract.\n')
        
        if len(contract_function_models) > 0:
            f.write('import pydantic\n\n')
            f.write('import typing\n\n')
            f.write('from openabi.contract_client import ContractClient\n\n\n')
            f.write(f'class {contract_name}Client(ContractClient):\n')
            f.write(f'\tABI = """{contract_abi_string}"""\n')

        for i in contract_function_models:
            function_string = generate_class_function_implementation(i, ['self'])
            function_string = update_each_non_empty_line(function_string, prefix='\t')
            f.write(function_string)
    
    #TODO: Run configured linting after generating code

if __name__ == '__main__':
    contract_name = 'ECR20'

    with open(f'examples/{contract_name}.json', 'r') as f:
        contract_abi_string = f.read()
    
    generate(contract_name=contract_name, contract_abi_string=contract_abi_string)