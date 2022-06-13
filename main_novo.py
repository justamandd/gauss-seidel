from modules import file as f, gauss as g, treat_matrix as treat

matrix = f.read_system_from_file('test_system.txt')
matrix = treat.separate_system_elements(matrix)
matrix = treat.group_system_unknowns(matrix)
letters = treat.get_matrix_letters(matrix)
matrix = treat.normalize_matrix(letters, treat.verify_unknowns_matrix(letters, matrix), matrix)
matrix = treat.order_by_unknown(letters, matrix)
matrix = treat.transform_unknowns_letters(matrix)
matrix = treat.join_parse_elements(matrix)


print(matrix)
