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
    
    final_matrix = []
    line = []
    elem = []

    for line in gross_matrix:
        for index in range(len(line)):
            if index == 0 and line[index] == '-':
                for sub_index in range(index,len(line)):
                    if sub_index != index and 


            if line[index] == '-':
                for sub_index in range(index,len(line)):
                    


    # return gross_matrix