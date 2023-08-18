def square_matrix_simple(matrix=[]):

    result_matrix = []
    
    for row in matrix:
        squared_row = []
        
        for num in row:
            squared_value = num ** 2
            squared_row.append(squared_value)
        
        result_matrix.append(squared_row)
    
    return result_matrix
