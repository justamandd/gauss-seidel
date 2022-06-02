def multiplicar_elementos_linha(linha, multiplicador):
    """This function receive a matrix line and multiplies it by a received multiplier

    Args:
        linha (List): matrix line
        multiplicador (Number): number to multiplie line

    Returns:
        List: multiplied line
    """
    replica_linha = list(linha)
    for indice in range(len(linha)):
        replica_linha[indice] = replica_linha[indice] * multiplicador
    return replica_linha

def soma_linhas(linha_base, linha_somada, multiplicador):
    """this func call multiplicar_linha for linha_base with multiplicador and the return sum to linha_somada

    Args:
        linha_base (List): line to multiplie
        linha_somada (List): line to sum with linha_base
        multiplicador (Number): num to multiplie linha_base

    Returns:
        List: the result of linha_somada + linha_base
    """
    linha_base_replica = multiplicar_elementos_linha(list(linha_base), multiplicador)
    linha_somada_replica = list(linha_somada)
    for elem_linha_base_multiplicada in range(len(linha_base_replica)):
        for elem_linha_somada in range(len(linha_somada_replica)):
            if elem_linha_base_multiplicada == elem_linha_somada:
                linha_somada_replica[elem_linha_somada] += linha_base_replica[elem_linha_base_multiplicada]
    return linha_somada_replica


def divide(linha, divisor):
    """this func divide each element of linha by divisor

    Args:
        linha (List): matrix line
        divisor (Number): num to divide linha

    Returns:
        List: result of linha / divisor
    """
    linha_replica = list(linha)
    for elem_linha in range(len(linha_replica)):
        if linha_replica[elem_linha] == 0:
            continue
        else:
            linha_replica[elem_linha] /= divisor
    return linha_replica

def divide_lines(primeira_linha, segunda_linha):
    """Essa função é responsável por dividir cada elemento da primeira linha pelo elemento de mesmo indice da segunda linha

    Args:
        primeira_linha (List): lista contendo elementos da primeira lista
        segunda_linha (List): lista contendo elementos da segunda lista

    Returns:
        quociente (List): coeficiente da divisão de cada elemento
    """
    primeira_linha_replica = list(primeira_linha)
    segunda_linha_replica = list(segunda_linha)
    quociente = []
    for elem_primeira_linha in range(len(primeira_linha_replica)):
        for elem_segunda_linha in range(len(segunda_linha_replica)):
            if elem_primeira_linha == elem_segunda_linha:
                if primeira_linha[elem_primeira_linha] == 0 or segunda_linha_replica[elem_segunda_linha] == 0:
                    quociente.append(0)
                else:
                    quociente.append(primeira_linha_replica[elem_primeira_linha] / segunda_linha_replica[elem_segunda_linha])
    return quociente

def permutacao(matriz):
    if len(matriz) == 0:
        return []

    if len(matriz) == 1:
        return [matriz]

    l = []

    for index in range(len(matriz)):
        m = matriz[index]

        tst_list = matriz[:index] + matriz[index+1:]
        for p in permutacao(tst_list):
            l.append([m] + p)

    return l

def diagonal_principal(matriz):
    """save the values of the main diagonal

    Args:
        matriz (List): the matriz that it will set the main diagonal

    Returns:
        List: main diagonal elements
    """
    diag_principal = []
    for linha in matriz:
        for index in range(len(linha)-1):
            if index == matriz.index(linha):
                diag_principal.append(linha[index])
    return diag_principal

def verifica_zero_diag_principal(matriz):
    """Verify if there is zero on main diag

    Args:
        matriz (List): matriz

    Returns:
        Boolean: if there is 0 in main diagonal returns True
    """
    there_is_zero = False
    diag_principal = diagonal_principal(matriz)
    for num in diag_principal:
        if num == 0:
            there_is_zero = True
    return there_is_zero

def seleciona_matriz_sem_zero(matriz):
    """Essa função é responsável de escolher uma possibilidade quando elementos da diagonal principal forem diferentes de 0

    Args:
        matriz (List): lista contendo as possibilidas da matriz permutada

    Returns:
        tentativa (List): matriz sem zeros na diagonal principal
    """
    possibilidades = permutacao(matriz)
    for tentativa in possibilidades:
        if not verifica_zero_diag_principal(tentativa):
            return tentativa

def gauss_elimination(possibilidades):
    """Essa função é responsável por aplicar o método de gauss na matriz para obter os valores das incognitas. Ele divide a primeira linha pelo primeiro elemento e parte para zerar todos abaixo, após zerar o numero abaixo ele divide a linha pelo primeiro elemento diferente de 0 afim de obter 1 na diag principal. Ele volta zerando o triângulo superior assim obtendo o resultado

    Args:
        matriz (List): matriz contendo as linhas a serem calculadas.

    Returns:
        matriz: ele retorna a nova matriz já escalonada
    """
    # direction -> up to down
    index_column = 0

    matriz = seleciona_matriz_sem_zero(possibilidades)

    for index_line in range(len(matriz)):
        if index_line == 0:
            matriz[0] = divide(matriz[index_line],matriz[index_line][index_column])

        for outra_linha in range(len(matriz)):
            # ele sempre 
            if outra_linha > index_line:
                if matriz[outra_linha][index_column] != 0:
                    if matriz[outra_linha][index_column] == matriz[index_line][index_column]:
                        matriz[outra_linha] = soma_linhas(
                            matriz[index_line], matriz[outra_linha], -1)
                    else:
                        matriz[outra_linha] = soma_linhas(
                            matriz[index_line], matriz[outra_linha], -matriz[outra_linha][index_column])
                    if matriz[outra_linha][index_column+1] != 1:
                        matriz[outra_linha] = divide(
                            matriz[outra_linha], matriz[outra_linha][index_column+1])
        index_column += 1
        
    #direction -> down to up
    index_column = len(matriz[0])-2
    for index_line in range(-1, -len(matriz)-1, -1):
        if index_line == -1:
            matriz[index_line] = divide(
                matriz[index_line], matriz[index_line][index_column])
        for outra_linha in range(-1, -len(matriz)-1, -1):
            if outra_linha < index_line:
                if matriz[outra_linha][index_column] != 0:
                    if matriz[outra_linha][index_column] == matriz[index_line][index_column]:
                        matriz[outra_linha] = soma_linhas(
                            matriz[index_line], matriz[outra_linha], -1)
                    else:
                        matriz[outra_linha] = soma_linhas(
                            matriz[index_line], matriz[outra_linha], -matriz[outra_linha][index_column])
        index_column -= 1
    return matriz

def verifica_se_possivel(matriz):
    """Essa função é responsável por testar caso a matriz é possivel dividindo elementos de mesmo indice e comparando o resultado, caso forem diferentes ela é possivel.

    Args:
        matriz (List): matriz contendo elementos a serem testados

    Returns:
        possivel (Boolean): caso possivel retorna True senão False
    """
    possivel = False
    
    for line in matriz:
        for other_line in matriz:
            if other_line == line:
                continue
            else:
                coeff = divide_lines(line[:len(line)-1],other_line[:len(line)-1])
                isequal = []
                for index in range(len(coeff)):
                    if index == len(coeff)-1:
                        break
                    else:
                        if coeff[index] == coeff[index+1]:
                            isequal.append(False)
                        else:
                            isequal.append(True)
                for index in isequal:
                    if index == True:
                        possivel = True 
                        break           
        if matriz[matriz.index(line)] == len(matriz)-1:
            break
    return possivel