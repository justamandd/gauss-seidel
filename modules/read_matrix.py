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
    elements_line = []

    #separates every elem in line text into a separated elem
    for line in gross_matrix:
        line_elem = []
        for text in line:
            for elem in text:
                line_elem.append(elem)
        elements_line.append(line_elem)


    #groups all elements before from letter
    lines = []
    for line in elements_line:
        line_elem = []
        coefficient = []
        for elem in range(len(line)):
            if line[elem].isalpha():
                coefficient.append(line[elem])
                line_elem.append(coefficient)
                coefficient = []
            elif line[elem] == '=':
                for sub_elem in range(elem+1, len(line)):
                    coefficient.append(line[sub_elem])
                line_elem.append(coefficient)
                coefficient = []
            else:
                coefficient.append(line[elem])
                if elem == len(line)-1:
                    coefficient = []
        lines.append(line_elem)
  
    lines = ordenar_por_coeff(normalizar_matriz(lines))

    #removes the letters and tranform alone letters into 1
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

    #join elements and parse into int
    for line in lines:
        for coeff in line:
            final_coeff = ''
            for elem in coeff:
                final_coeff += elem
            line[line.index(coeff)] = int(final_coeff)

    return lines

def normalizar_matriz(matriz):
    """this function add missing coefficients

    Args:
        matriz (List): list with all coefficients

    Returns:
        matriz: normalizated matrix
    """
    letters = obter_letras_matriz(matriz)
    matriz_replica = list(matriz)

    for line in matriz_replica:
        possui_coeff = []
        for coeff in line:
            for elem in coeff:
                if elem.isalpha():
                    for letter in letters:
                        if elem == letter:
                            possui_coeff.append(letter)
        if possui_coeff != letters:
            diff = set(letters).difference(set(possui_coeff))
            for coeff in diff:
                line.insert(len(line)-1,['0',coeff])
        
    return matriz_replica

def obter_letras_matriz(matriz):   
    """this function saves all letters found in matriz

    Args:
        matriz (List): matriz base

    Returns:
        Lines (List): all letters found in matriz
    """
    letters = []
    for line in matriz:
        for coeff in line:
            for elem in coeff:
                if elem.isalpha():
                    letters.append(elem)

    lines = sorted(list(set(letters)))
    return lines

def ordenar_por_coeff(matriz):
    """this function ordenate by coefficient

    Args:
        matriz (Lisst): base matriz

    Returns:
        matriz_ordenada: matriz ordenated by letter sorting
    """
    matriz_ordenada = []
    
    letters = obter_letras_matriz(matriz)

    for line in matriz:
        linha = []
        for letter in letters:
            for coeff in range(len(line)):
                if line[coeff][len(line[coeff])-1] == letter:
                    linha.append(line[coeff])
        linha.append(line[len(line)-1])
        
        matriz_ordenada.append(linha)
    return matriz_ordenada