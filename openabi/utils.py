import re

def camel_to_snake(camel_string):
    snake_string = re.sub('([A-Z])', r'_\1', camel_string).lower()
    return snake_string

def update_each_non_empty_line(string: str, prefix: str) -> str:
    lines = string.split("\n")
    lines = [prefix + line if line else line for line in lines]
    return "\n".join(lines)

