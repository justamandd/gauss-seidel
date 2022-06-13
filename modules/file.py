""""
module: file
objective: read
"""

from os import path


def read_system_from_file(file_name):
    linear_system = []
    with open(path.abspath(f'linear_systems/{file_name}'), 'r') as file:
        for equation in file:
            linear_system.append(equation.replace('\n', ''))
        return linear_system
