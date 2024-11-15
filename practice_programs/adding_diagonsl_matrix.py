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
print("Matrix A")
for a in matrix_A:
    print(a)

print("Now add the diagonal elment in the matrix")

n = len(matrix_A)

primary_diag = 0
secondary_diag = 0
for i in range(n):
    primary_diag += int(matrix_A[i][i])
    secondary_diag += int(matrix_A[i][n - i - 1])



total_sum = primary_diag + secondary_diag
print("primary diagonal : ",primary_diag)
print("secondary diagonal", secondary_diag)
print("total digonal : ", total_sum)