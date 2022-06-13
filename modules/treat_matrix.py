""""
module: treat_matrix
objective: treat matrix
"""


def separate_system_elements(system):
    system_lines = []
    for line in system:
        line_elements = []
        for text in line:
            for element in text:
                line_elements.append(element)
        system_lines.append(line_elements)
    return system_lines


def group_system_unknowns(separated_system):
    grouped_system = []
    for equation in separated_system:
        line = []
        unknown = []
        for element in range(len(equation)):
            if equation[element].isalpha():
                line.append(unknown+[equation[element]])
                unknown = []
            elif equation[element] == '=':
                for after_equal_index in range(element + 1, len(equation)):
                    unknown.append(equation[after_equal_index])
                line.append(unknown)
                unknown = []
            else:
                unknown.append(equation[element])
                if element == len(equation)-1:
                    unknown = []
        grouped_system.append(line)
    return grouped_system


def get_matrix_letters(matrix):
    letters = []
    for system in matrix:
        for unknown in system:
            for element in unknown:
                if element.isalpha():
                    letters.append(element)
    return sorted(list(set(letters)))


def order_by_unknown(letters, matrix):
    ordered_matrix = []
    for equation in matrix:
        line = []
        for letter in letters:
            for unknown in range(len(equation)):
                if equation[unknown][len(equation[unknown])-1] == letter:
                    line.append(equation[unknown])
        line.append(equation[len(equation)-1])
        ordered_matrix.append(line)
    return ordered_matrix


def verify_unknowns_matrix(letters_matrix, matrix):
    letters_lines = []
    for line in matrix:
        has_letter = []
        for unknown in line:
            for element in unknown:
                if element.isalpha():
                    for letter in letters_matrix:
                        if element == letter:
                            has_letter.append(letter)
        letters_lines.append(has_letter)
    return letters_lines


def normalize_matrix(letters_matrix, letters_line, matrix):
    replica_matrix = list(matrix)
    for equation in replica_matrix:
        if letters_line[replica_matrix.index(equation)] != letters_matrix:
            missing_letters = set(letters_matrix).difference(set(letters_line[replica_matrix.index(equation)]))
            for unknown in missing_letters:
                equation.insert(len(equation) - 1, ['0', unknown])
    return replica_matrix


def transform_unknowns_letters(grouped_system):
    for equation in grouped_system:
        for unknown in equation:
            for element in unknown:
                if element.isalpha():
                    unknown.remove(element)
                    if len(unknown) == 0:
                        unknown.append(1)
                    elif len(unknown) == 1:
                        if unknown[0] == '-':
                            unknown.append('1')
    return grouped_system


def join_parse_elements(grouped_system):
    for equation in grouped_system:
        for unknown in equation:
            new_unknown = ''
            for element in unknown:
                new_unknown += str(element)
            equation[equation.index(unknown)] = int(new_unknown)
    return grouped_system
