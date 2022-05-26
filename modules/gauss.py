def multiplica_linha(linha, multiplicador):
    replica_linha = list(linha)
    for indice in range(len(linha)):
        replica_linha[indice] = replica_linha[indice] * multiplicador
    return replica_linha


def soma_linha(linha_multi, linha_somada, multiplicador):
    linha_multi_replica = multiplica_linha(list(linha_multi), multiplicador)
    linha_somada_replica = list(linha_somada)
    for l_mult in range(len(linha_multi_replica)):
        for l_som in range(len(linha_somada_replica)):
            if l_mult == l_som:
                linha_somada_replica[l_som] += linha_multi_replica[l_mult]
    return linha_somada_replica


def divide(linha_divisor, divisor):
    linha_divisor_replica = list(linha_divisor)
    for l_div in range(len(linha_divisor_replica)):
        if linha_divisor_replica[l_div] == 0:
            continue
        else:
            linha_divisor_replica[l_div] /= divisor
    return linha_divisor_replica


def permutacao(matriz):
    if len(matriz) == 0:
        return []

    if len(matriz) == 1:
        return [matriz]

    l = []

    for index in range(len(matriz)):
        m = matriz[index]

        remLst = matriz[:index] + matriz[index+1:]
        for p in permutacao(remLst):
            l.append([m] + p)

    return l


def diagonal_principal(matrix):
    """save the values of the main diagonal

    Args:
        matrix (List): the matrix that it will set the main diagonal

    Returns:
        List: main diagonal elements
    """
    main_diag = []
    for line in matrix:
        for i in range(0, len(line)-1):
            if i == matrix.index(line):
                main_diag.append(line[i])
    return main_diag


def verifica_zero_diag_principal(matrix):
    """Verify if there is zero on main diag

    Args:
        matrix (List): matrix

    Returns:
        Boolean: if there is 0 in main diagonal returns True
    """
    there_is_zero = False
    main_diag = diagonal_principal(matrix)
    for num in main_diag:
        if num == 0:
            there_is_zero = True
    return there_is_zero

def seleciona_matriz_sem_zero(matriz):
    possibilidades = permutacao(matriz)
    for tentativa in possibilidades:
        if verifica_zero_diag_principal(tentativa) == False:
            return tentativa

def gauss_elimination(matriz):
    # direction -> up to down
    index_column = 0
    for index_line in range(len(matriz)):
        matriz = seleciona_matriz_sem_zero(matriz)
        if index_line == 0:
            matriz[0] = divide(matriz[index_line],matriz[index_line][index_column])
        for sub_line in range(len(matriz)):
            if sub_line > index_line:
                if matriz[sub_line][index_column] != 0:
                    if matriz[sub_line][index_column] == matriz[index_line][index_column]:
                        matriz[sub_line] = soma_linha(
                            matriz[index_line], matriz[sub_line], -1)
                    else:
                        matriz[sub_line] = soma_linha(
                            matriz[index_line], matriz[sub_line], -matriz[sub_line][index_column])
                    if matriz[sub_line][index_column+1] != 1:
                        matriz[sub_line] = divide(
                            matriz[sub_line], matriz[sub_line][index_column+1])
        index_column += 1
    #direction -> down to up
    index_column = len(matriz[0])-2
    for index_line in range(-1, -len(matriz)-1, -1):
        if index_line == -1:
            matriz[index_line] = divide(
                matriz[index_line], matriz[index_line][index_column])
        for sub_line in range(-1, -len(matriz)-1, -1):
            if sub_line < index_line:
                if matriz[sub_line][index_column] != 0:
                    if matriz[sub_line][index_column] == matriz[index_line][index_column]:
                        matriz[sub_line] = soma_linha(
                            matriz[index_line], matriz[sub_line], -1)
                    else:
                        matriz[sub_line] = soma_linha(
                            matriz[index_line], matriz[sub_line], -matriz[sub_line][index_column])
        index_column -= 1
    return matriz