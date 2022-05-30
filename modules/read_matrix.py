from os import path

def read_matriz_txt(file_name):
    """This is a function that get a external file 
    by path + file_name then makes a matrix line by line and then return 

    Args:
        file_name (string): txt archive file name

    Returns:
        List: matrix of the lines of the archive
    """
    gross_matrix = []

    with open(path.abspath(f'matrix_files/{file_name}'), 'r') as file:
        for line in file:
            if line.find('\n') != False:
                line = line.replace('\n','')
                gross_matrix.append([line])
            else:
                gross_matrix.append([line])
    return gross_matrix

def treat_matrix(gross_matrix):
    elements = []
    lin = []
    for line in gross_matrix:
        for text in line:
            for elem in text:
                lin.append(elem)
        elements.append(lin)
        lin = []

    var = []

    lines = []

    for line in elements:
        for elem in range(len(line)):
            if line[elem].isalpha():
                var.append(line[elem])
                lin.append(var)
                var = []
            elif line[elem] == '=':
                for sub_elem in range(elem+1, len(line)):
                    var.append(line[sub_elem])
                lin.append(var)
                var = []
            else:
                var.append(line[elem])
                if elem == len(line)-1:
                    var = []
        lines.append(lin)
        lin = []

    # para tratar divergências de qtd de incognitas e ondem tem que ser aq (lines)

    normalizar_matriz(lines)
    print(lines)


    for line in lines:
        for coeff in line:
            for elem in coeff:
                if elem.isalpha():
                    coeff.remove(elem)
                    if len(coeff) == 0:
                        coeff.append('1')
                    elif len(coeff) == 1:
                        if coeff[0] == '-':
                            coeff.append('1')
    for line in lines:
        for coeff in line:
            final_coeff = ''
            for elem in coeff:
                final_coeff += elem
            line[line.index(coeff)] = int(final_coeff)
    
    return lines

def normalizar_matriz(matriz):
    letters = obter_letras_matriz(matriz)
    
    for line in matriz:
        possui_coeff = []
        for coeff in line:
            for elem in coeff:
                if elem.isalpha():
                    for letter in letters:
                        if elem == letter:
                            possui_coeff.append(letter)
        if possui_coeff == letters:
            continue
        else:
            diff = set(letters).difference(set(possui_coeff))
            for coeff in diff:
                line.insert(len(line)-1,['0',coeff])

    # print(letters)

def obter_letras_matriz(matriz):
    letters = []

    for line in matriz:
        for coeff in line:
            for elem in coeff:
                if elem.isalpha():
                    letters.append(elem)

    return sorted(list(set(letters)))


def ordenar_por_coeff(matriz):
    matriz_ordenada = []
    
    letters = obter_letras_matriz(matriz)

    for line in matriz:
        
