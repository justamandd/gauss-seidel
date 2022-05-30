from modules.gauss import gauss_elimination, permutacao, verifica_se_possivel
from modules.read_matrix import read_matriz_txt, treat_matrix

# matriz = [[0.0,3.0,2.0,28.0],
        #   [4.0,0.0,2.0,24.0],
        #   [2.0,3.0,0.0,16.0]]

# matriz = [[2,3,4],
#                   [1,-5,2]]

# matriz = [[1, 1, 7],
#                   [1, 2, 9]]

# matriz = [[4,0,2,24],
#           [2,3,0,16],
#           [0,3,2,28]]

# matriz = [[0,3,2,9],
#           [1,0,4,14],
#           [0,1,1,4]]

# matriz = [[1,2,1,12],
#           [1,-3,5,1],
#           [2,-1,3,10]]

# matriz = [[2,0,0,5,19],
#           [3,1,0,2,17],
#           [4,2,7,1,28],
#           [5,3,2,2,33]]

# dá erro por algm motivo
# matriz = [[1,1,1,-1,6],
#           [2,1,-2,1,-1],
#           [1,-2,1,2,-3],
#           [1,1,1,1,2]]

matriz = read_matriz_txt('teste.txt')

# for line in matriz:
#     print(line)

matriz = treat_matrix(matriz)

# for line in matriz:
#     print(line)

# matriz = gauss_elimination(matriz)

# print(verifica_se_possivel(matriz))


for line in matriz:
    print(line)
