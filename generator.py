import json
import re 
import typing

from contract_model import EventAttribute, FunctionAttribute, SolidityType, Argument

SOLIDITY_TO_PYTHON_MAPPING = {
    'uint256': 'int',
    'bytes32': 'bytes',
    'address': "pydantic.constr(regex=r'^0x[0-9a-fA-F]{40}$')",
    'uint8': 'int',
    'bool': 'bool',
    'string': 'str'
}

CLASS_SEPERATOR = '\n\n\n'
FUNCTION_SEPERATOR = '\n'
ATTRIBUTE_SEPERATOR = "\n\t"

def convert_to_python_type(solidity_type: SolidityType):
    python_type_string =  SOLIDITY_TO_PYTHON_MAPPING.get(solidity_type)

    if python_type_string is None:
        raise NotImplementedError(f"Not supported {solidity_type} solidity type! add to mapping")
    
    return python_type_string

def camel_to_snake(camel_string):
    snake_string = re.sub('([A-Z])', r'_\1', camel_string).lower()
    return snake_string

def convert_to_python_code_style(name: str):
    snake_case_name = camel_to_snake(name)

    if snake_case_name in ['from']:
        return snake_case_name + '_'
    return snake_case_name

def generate_typed_dict_string(name: str, arguments: typing.List[Argument]) -> str:
    fields = [f"{field.name}={convert_to_python_type(field.type)}" for field in arguments]

    return f'typing.TypedDict("{name}", {", ".join(fields)})'

def generate_function_return_type_name(function_name:str) -> str:
    return function_name + '_output'

def generate_event_models(event_data_model: EventAttribute):
    properties_strings = []

    for argument in event_data_model.inputs:
        properties_strings.append(
            f"{convert_to_python_code_style(argument.name)}: {convert_to_python_type(argument.type)}" 
        )
    
    properties_generated_string = ATTRIBUTE_SEPERATOR.join(properties_strings)

    return f'''class {event_data_model.name}(pydantic.BaseModel):\n\t{properties_generated_string}'''

def generate_class_function_implementation(function_data_model: FunctionAttribute):
    # Extract the function's name and arguments from the ABI
    function_name = function_data_model.name
    base_signature_arguments = ['self']
    base_signature_arguments.extend(f"{input.name}: {convert_to_python_type(input.type)}" for input in function_data_model.inputs)
    function_signature = ", ".join(base_signature_arguments)
    args = [input.name for input in function_data_model.inputs]

    return_type = None
    return_type_type_string = ''

    if len(function_data_model.outputs) == 0: # no output to the function
        return_type = None
    elif len(function_data_model.outputs) == 1 and function_data_model.outputs[0].name == '': # single output without naming
        return_type = convert_to_python_type(function_data_model.outputs[0].type)
    else: # 1 or more outputs with names
        return_type = generate_function_return_type_name(function_name)
        return_type_string = generate_typed_dict_string(return_type, function_data_model.outputs)
        return_type_type_string = f"{return_type} = {return_type_string}"
    
    implementation = ''

    if return_type_type_string != '':
        implementation += f"\t{return_type_type_string}\n"
    
    # Generate the function signature
    implementation += f"\tdef {convert_to_python_code_style(function_name)}({function_signature}) -> {return_type}:\n"

    # Generate the function body
    implementation += f"\t\tresult = self._contract_api.functions.{function_name}({', '.join(args)}).call()\n\n"

    implementation += "\t\treturn result\n"

    return implementation 

def generate(contract_name: str, contract_abi_string: str):
    
    contract_description = json.loads(contract_abi_string)
    contract_events_models = [EventAttribute.parse_obj(i) for i in contract_description if i['type'] == 'event']

    with open('generated/events.py', 'w') as f:
        f.truncate()

        if len(contract_events_models) > 0:
            f.write('import pydantic')

        for i in contract_events_models:
            event_class_string = generate_event_models(i)
            f.write(CLASS_SEPERATOR)
            f.write(event_class_string)
        
        f.write('\n') # end of file space

    contract_function_models = [FunctionAttribute.parse_obj(i) for i in contract_description if i['type'] == 'function']
    
    with open('generated/api.py', 'w') as f:
        f.truncate()
        
        f.write('# This file is generated using the Etheruem API generator.\n# the file contains the basic functions for interacting with ethereum contract.\n')
        
        if len(contract_function_models) > 0:
            f.write('import pydantic\n\n')
            f.write('import typing\n\n')
            f.write('from contract_client import ContractClient\n\n\n')
            f.write(f'class {contract_name}Client(ContractClient):\n')
            f.write(f'\tABI = """{contract_abi_string}"""\n')

        for i in contract_function_models:
            function_string = generate_class_function_implementation(i)
            f.write(function_string)
            f.write(FUNCTION_SEPERATOR)

if __name__ == '__main__':
    contract_name = 'ECR20'

    with open(f'examples/{contract_name}.json', 'r') as f:
        contract_abi_string = f.read()
    
    generate(contract_name=contract_name, contract_abi_string=contract_abi_string)