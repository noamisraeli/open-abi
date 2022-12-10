import json
import re 

import pydantic

from contract_model import EventAttribute, FunctionAttribute, SolidityType

UInt256 = int
Bytes32 = bytes
Address = pydantic.constr(regex=r'^0x[0-9a-fA-F]{40}$')

SOLIDITY_TO_PYTHON_MAPPING = {
    'uint256': 'int',
    'bytes32': 'bytes',
    'address': "pydantic.constr(regex=r'^0x[0-9a-fA-F]{40}$')",
    'unit8': 'int',
    'bool': 'bool'
}


CLASS_SEPERATOR = '\n\n\n'
FUNCTION_SEPERATOR = '\n\n'
ATTRIBUTE_SEPERATOR = "\n\t"

def convert_to_python_type(solidity_type: SolidityType):
    return SOLIDITY_TO_PYTHON_MAPPING.get(solidity_type)

def convert_to_python_compatible_name(name: str):
    if name in ['from']:
        return name + '_'
    return name

def camel_to_snake(camel_string):
    snake_string = re.sub('([A-Z])', r'_\1', camel_string).lower()
    return snake_string

def convert_to_python_code_style(function_name: str):
    return camel_to_snake(function_name)

def generate_data_models(event_data_model: EventAttribute):
    properties_strings = []
    for argument in event_data_model.inputs:
        properties_strings.append(
            f"{convert_to_python_compatible_name(argument.name)}: {convert_to_python_type(argument.type)}" 
        )
    properties_generated_string = ATTRIBUTE_SEPERATOR.join(properties_strings)

    return f'''class {event_data_model.name}(pydantic.BaseModel):\n\t{properties_generated_string}'''

def generate_function_definitions(function_data_model: FunctionAttribute):
    function_signature = ", ".join(f"{input.name}: {convert_to_python_type(input.type)}" for input in function_data_model.inputs)
    function_name = convert_to_python_code_style(function_data_model.name)

    return f"""def {function_name}({function_signature}):\n\tpass # Implementation needed!"""

if __name__ == '__main__': 
    with open('examples/ECR20.json', 'r') as f:
        contract_description = json.load(f)
    
    contract_events_models = [EventAttribute.parse_obj(i) for i in contract_description if i['type'] == 'event']


    with open('generated/events.py', 'w') as f:
        f.truncate()

        if len(contract_events_models) > 0:
            f.write('import pydantic')

        for i in contract_events_models:
            event_class_string = generate_data_models(i)
            f.write(CLASS_SEPERATOR)
            f.write(event_class_string)
        
        f.write('\n') # end of file space

    contract_function_models = [FunctionAttribute.parse_obj(i) for i in contract_description if i['type'] == 'function']
    
    with open('generated/api.py', 'w') as f:
        f.truncate()
        
        f.write('# This file is generated using the Etheruem API generator.\n \
                # the file contains the basic functions for interacting with ethereum contract.\n')
        
        if len(contract_events_models) > 0:
            f.write('import pydantic')
            f.write(FUNCTION_SEPERATOR)

        for i in contract_function_models:
            function_string = generate_function_definitions(i)
            f.write(function_string)
            f.write(FUNCTION_SEPERATOR)

        