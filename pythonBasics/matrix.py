
# print 2nd row 2nd column value in the list in the list (matrix)

mat1 = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

print(mat1[1][1])

#To read the last element from each row.
for i in range(len(mat1)):
    print(mat1[i][-1])

# Adding two Matrices

mat2 = [[7, 16, -6],
        [9, 20, -4],
        [-1, 3, 27]]

mat3 = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]
matrix_length = len(mat1)

# To Add mat1 and mat2 matrices
for i in range(len(mat1)):
    for j in range(len(mat2)):
        mat3[i][j] = mat1[i][j] + mat2[i][j]

    # To Print the matrix
print("The sum of Matrix mat1 and mat2 = ", mat3)

print("************************************")
