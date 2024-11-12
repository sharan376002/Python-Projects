# print("Matrix Multiplication operation")
# row =int(input("Enter the number of rows  : "))
# col =int(input("Enter the number of col  : "))

matrix_A = [[2,0,0],
            [0,0,0],
            [0,0,0,]]
# print("Enter the values of matrix A : ")
# for i in range(row+1):
#     for j in range(col+1):
#         matrix_A[i][j] = input(f"Enter the value of a{i}{j} ")
# print("\n")
# print("Matrix A")
# for a in matrix_A:
#     print(a)

matrix_B = [[2,0,0],
            [0,0,0],
            [0,0,0,]]

# print("Enter the values of matrix B : ")
# for i in range(row+1):
#     for j in range(col+1):
#         matrix_B[i][j] = input(f"Enter the value of b{i}{j} ")

# print("\n")
# print("Matrix B")
# for b in matrix_B:
#     print(b)





product = [[0,0,0],
           [0,0,0],
        [0,0,0,]]

for i in range(len(matrix_A)):
    for j in range(len(matrix_B[0])):
        for k in range(len(matrix_B)):
            product[i][j] += matrix_A[i][k] * matrix_B[k][j]
    

print("\n")

print("multiplied Matrix")
for s in product:

    print(s)


