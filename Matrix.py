matrix_size = str(input("Enter the size of the matrix [m x n]: "))

matrix_row = int(matrix_size.split()[0])
matrix_column = int(matrix_size.split()[2])

lan = []
for i in range(matrix_column):
    lan.append(i+1)

a = len(lan)
i = 0
while i < a:
    if i == 0:
        lan[i] = "first"
    elif i < a-1:
        lan[i] = "next"
    else:
        lan[i] = "last"

    i += 1

row_num = 1
matrix = []
for i in range(matrix_row):
    matrix_list = []
    for i in range(matrix_column):
       matrix_list.append(int(input(f"Enter the {lan[i]} diget in row {row_num}: ")))
    matrix.append(matrix_list)
    row_num += 1

print(" ")
print("The matrix you entered is...")
for one_of_the_rows in matrix:
    print(one_of_the_rows)

# 2 hours in on Jan 18, 2024. Begining to program the Row Reduction Algorithm

# Step. 1: Begin with an m × n matrix A. If A=0,the matrix is in RREF 
is_matrix_all_zeros = 0
for row in range(matrix_row):
    for column in range(matrix_column):
        if matrix[row][column] == 0:
           is_matrix_all_zeros += 1
if is_matrix_all_zeros == (matrix_column*matrix_row):
    print(" ")
    print("The matrix is already in RREF") 
    exit()

# Step. 2: Determine the leftmost non-zero column.
pivot = [] 
def find_pivot(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[j][i] != 0:
                pivot.append(matrix[j][i])
                pivot.append(j)
                pivot.append(i)
                return pivot
find_pivot(matrix)

# Step. 3: use the elemetry row opperations to put a 1 in the top most position
def scale(x, y):
    for i in range(len(matrix[x])):
        matrix[x][i] = matrix[x][i] * y
    return matrix
    # x = which row, y = scale by how much
scale(pivot[1], (1/matrix[pivot[1]][pivot[2]]))


def interchange(x, y):
    matrix[x], matrix[y] = matrix[y], matrix[x]
    return matrix
    # x = row 1 swapping with y = row 2
interchange(pivot[1], 0)

# Step. 4: Use elementary row operations to put zeros below the pivot position.
def replacement(x, y, z):
    matrix_replacement = matrix[y][z] * -matrix[x][z]
    for i in range(len(matrix[0])):
        matrix[x][i] = matrix_replacement*matrix[y][i] + matrix[x][i]
    return matrix
    # x = which row is being replaced, y = which row to use, z = which column to use
for i in range(1, matrix_row):
    if matrix[i][pivot[1]] != 0:
        replacement(i, 0, 0)


# Apply Step 2-4 to the submatrix consisting of the rows that lie (strictly below) the pivot position.
def keep_going(matrix):
    for x in range(1, matrix_row):
        
        def all_zero(matrix):
            for i in range(x, len(matrix)):
                for j in range(x, len(matrix[i])):
                    if matrix[j][i] != 0:
                        return 
            print(" ")
            print("The matrix in RREF is...")
            for one_of_the_rows in matrix:
                print(one_of_the_rows) 
            exit()
        all_zero(matrix)


        pivot_x = [] 
        def find_pivot_i(matrix):
            for i in range(x, len(matrix)):
                for j in range(x, len(matrix[i])):
                    if matrix[j][i] != 0:
                        pivot_x.append(matrix[j][i])
                        pivot_x.append(j)
                        pivot_x.append(i)
                        return pivot
        find_pivot_i(matrix)
        

        def scale(x, y):
            for i in range(len(matrix[x])):
                matrix[x][i] = round(matrix[x][i] * y, 5)
                if matrix[x][i] == -0.0:
                    matrix[x][i] = 0.0
            return matrix
        scale(pivot_x[1], (1/matrix[pivot_x[1]][pivot_x[2]]))


        def interchange(z, y):
            matrix[z], matrix[y] = matrix[y], matrix[z]
            pivot_x[1] = x
            return matrix
        interchange(pivot_x[1], x)
        
        
        def replacement(x, y, z):
            matrix_replacement = matrix[y][z] * -matrix[x][z]
            for i in range(len(matrix[0])):
                matrix[x][i] = round(matrix_replacement*matrix[y][i] + matrix[x][i], 5)
            return matrix
        

        # used to turn matrix into REF
        for i in range(matrix_column+1):
            if x+i < matrix_row:
                if matrix[x+i][pivot_x[1]] != 0 and matrix[x+i][pivot_x[1]] != 1:
                    replacement(x+i, pivot_x[1], pivot_x[2])
                    
        
        # used to turn REF to RREF
        for i in range(pivot_x[1]):
                if matrix[i][pivot_x[2]] != 0:
                    replacement(i, pivot_x[1], pivot_x[2])
                       

keep_going(matrix)
print(" ")
print("The matrix in RREF is...")
for one_of_the_rows in matrix:
    print(one_of_the_rows) 

#DONE (Approximatley ~24-30 hours of coding)

