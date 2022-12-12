import typing

from ..contract_model import EventAttribute, FunctionAttribute, SolidityType, Argument
from ..utils import camel_to_snake, update_each_non_empty_line


SOLIDITY_TO_PYTHON_MAPPING = {
    'uint256': 'int',
    'bytes32': 'bytes',
    'address': "pydantic.constr(regex=r'^0x[0-9a-fA-F]{40}$')",
    'uint8': 'int',
    'bool': 'bool',
    'string': 'str'
}

ATTRIBUTE_SEPERATOR = "\n\t"

def get_function_abi_signature(function_data_model: FunctionAttribute):
    return f"{function_data_model.name}({','.join([input.type for input in function_data_model.inputs])})"

def convert_to_python_type(solidity_type: SolidityType):
    python_type_string =  SOLIDITY_TO_PYTHON_MAPPING.get(solidity_type)

    if python_type_string is None:
        raise NotImplementedError(f"Not supported {solidity_type} solidity type! add to mapping")
    
    return python_type_string

def convert_to_python_code_style(name: str):
    snake_case_name = camel_to_snake(name)

    if snake_case_name in ['from']:
        return snake_case_name + '_'
    return snake_case_name

def generate_pydantic_class_string(name: str, arguments: typing.List[Argument]):
    properties_strings = []

    for argument in arguments:
        properties_strings.append(
            f"{convert_to_python_code_style(argument.name)}: {convert_to_python_type(argument.type)}" 
        )
    
    properties_generated_string = ATTRIBUTE_SEPERATOR.join(properties_strings)
    return f'''class {name}(pydantic.BaseModel):\n\t{properties_generated_string}'''

def generate_function_return_type_name(function_name: str) -> str:
    return function_name + '_output'

def generate_event_models(event_data_model: EventAttribute):
    return generate_pydantic_class_string(event_data_model.name, event_data_model.inputs)

def generate_class_function_implementation(function_data_model: FunctionAttribute, prefix_arguments: typing.Optional[typing.List[str]] = None):
    # Extract the function's name and arguments from the ABI
    function_name = function_data_model.name
    base_signature_arguments = prefix_arguments or []

    base_signature_arguments.extend(f"{input.name}: {convert_to_python_type(input.type)}" for input in function_data_model.inputs)
    function_signature = ", ".join(base_signature_arguments)
    args = [input.name for input in function_data_model.inputs]

    return_type = None
    return_type_class_string = ''

    if len(function_data_model.outputs) == 0:  
        return_type = None # no output to the function
    elif len(function_data_model.outputs) == 1 and function_data_model.outputs[0].name == '': # single output without naming
        return_type = convert_to_python_type(function_data_model.outputs[0].type)
    else: # 1 or more outputs with names
        return_type = generate_function_return_type_name(function_name)
        return_type_class_string = generate_pydantic_class_string(return_type, function_data_model.outputs)
        
    implementation = ''

    if return_type_class_string != '':

        implementation += f"{return_type_class_string}\n"
    
    # Generate the function signature
    implementation += f"def {convert_to_python_code_style(function_name)}({function_signature}) -> {return_type}:\n"

    implementation += f"\tfunction_abi_signature = '{get_function_abi_signature(function_data_model=function_data_model)}'\n"
    # Generate the function body
    implementation += f"\tresult = self.make_call(function_abi_signature, [{', '.join(args)}])\n\n"
    implementation += f"\t#TODO: use the eth.call method instead of the mockypatched web3py api\n"
    
    if return_type is not None and return_type_class_string != '':
        implementation += f"\treturn self.{return_type}(result)\n"
    else:
        implementation += f"\treturn result\n"

    return implementation 