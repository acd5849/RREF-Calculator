
matrix = [[1, 5, 10], [-1, 7, 14], [5, 8, 4]]

# [ 1, 5, 10]
# [ -1, 7, 14]
# [ 5, 8, 4]

def interchange(x, y):
    matrix[x], matrix[y] = matrix[y], matrix[x]
    return matrix
    # x = row 1 swapping with y = row 2

def scale(x, y):
    for i in range(len(matrix[x])):
        matrix[x][i] = matrix[x][i] * y
    return matrix
    # x = which row, y = scale by how much


#def replacement(x, y, z):
    #matrix_replacement = matrix[y][z] * -matrix[x][z]
    #print(matrix_replacement)
    #for i in range(len(matrix[x])):
        #matrix[x][i] = matrix_replacement + matrix[x][i]
    #return matrix
    
def replacement2(x, y, z):
    matrix_replacement = matrix[y][z] * -matrix[x][z]
    for i in range(len(matrix)):
        matrix[x][i] = round(matrix_replacement*matrix[y][i]) + matrix[x][i]
    return matrix
# x = which row is being replaced, y = which row to use, z = which column to use






# replacement(x+i, pivot_x[1], pivot_x[1])
# from (file name) import (function name) -> for just one function
# import (file name) -> for the entire file 
# you can use and and or in a single if statement
