#Name: Loc Nguyen
#CS3310 Project 1
import random
size = 2


#function to multiply matrix
def multiply(matrixA, matrixB, matrixC):
    for i in range(len(matrixA)):
        for j in range(len(matrixB)):
            matrixC[i][j] = 0
            for k in range(len(matrixC)):
                matrixC[i][j] += matrixA[i][k]*matrixB[k][j]
            
#function to print out matrix
def printMatrix(matrix, row, col):
    for i in range(row):
        for j in range(col):
            print(matrix[i][j], end = " ")
        print()
    print()
#initialize matrices with random number from 0 to 9 and matrixC with 0 then print out matrix for validation            
print("Matrix A")
matrixA = [[random.randint(0,9) for x in range(size)]for y in range (size)]
printMatrix(matrixA,size,size)
print("Matrix B")
matrixB = [[random.randint(0,9) for x in range(size)]for y in range (size)]
printMatrix(matrixB,size,size)           
matrixC = [[0 for x in range (size)]for y in range (size)]
multiply(matrixA,matrixB,matrixC)
print("Matrix C")
printMatrix(matrixC,size,size)