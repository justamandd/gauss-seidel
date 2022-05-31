from modules.gauss import gauss_elimination, verifica_se_possivel
from modules.read_matrix import read_matriz_txt, treat_matrix
from os import system

def clear_console():
    system('cls')

if __name__ == '__main__':
    matriz = []
    clear_console()
    tipo_leitura = input('Você deseja digitar a matriz ou inserir um arquivo? (D=Digitar/I=Inserir): ')
    if tipo_leitura.lower() == 'i':
        clear_console()
        nome_arquivo = input('Digite o nome do arquivo com a extensão: ')
        matriz = read_matriz_txt(nome_arquivo)
    elif tipo_leitura.lower() == 'd':
        digitar = 1
        clear_console()
        print('Digite 0 para sair do looping!')
        while digitar != '0':
            linha = input(f'Digite a {digitar} linha do sistema: ')
            if linha == '0':
                break
            else:
                matriz.append([linha.strip().lower()])
            digitar += 1
    else:
        print('Opção inválida!')

    clear_console()
    if len(matriz) != 0:
        print('Matriz base:')
        for line in matriz:
            print(line)
        matriz = treat_matrix(matriz)
        print('Matriz ampliada tratada:')
        for line in matriz:
            print(line)
        if verifica_se_possivel(matriz):
            matriz = gauss_elimination(matriz)
            print('Gauss-Seidel aplicado gerando:')
            for line in matriz:
                print(line)
        else:
            print('Matriz não é possivel de ser calculada')