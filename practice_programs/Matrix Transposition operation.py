print("Matrix Transportation operation")

row =int(input("Enter the number of rows  : "))
col =int(input("Enter the number of col  : "))

matrix_A = [[0,0,0],
            [0,0,0],
            [0,0,0,]]

print("Enter the values of matrix A : ")
for i in range(row+1):
    for j in range(col+1):
        matrix_A[i][j] = input(f"Enter the value of a{i}{j} ")
print("\n")
print("Matrix A without transpose")
for a in matrix_A:
    print(a)



transpose = [[0,0,0],
           [0,0,0],
        [0,0,0,]]

# for i in range(len(matrix_A)):
#     for j  in range(i+1, 9):
#         tanspose = matrix_A[i][j], matrix_A[j][i] = matrix_A[j][i] ,matrix_A[j][i]

transposed = [[matrix_A[j][i] for j in range(len(matrix_A))]  for i in range(len(matrix_A[0]))]

print("matrix With transpose")
print(transposed)