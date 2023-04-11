#Name: Loc Nguyen
#CS3310 Project 1
#Classical Matrix Multiplication 
import random,time

size = 64


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
trialTime = []
for i in range(10):
    print("Trial",i+1)
    start = time.time()
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
    #end of algo
    end = time.time()
    executionTime = end-start
    trialTime.append(executionTime)
#sort to find worst and best time to compute average time
trialTime.sort()
averageTime = (sum(trialTime)-trialTime[0] - trialTime[len(trialTime)-1])/(8)
print("Average time is %.5f" % averageTime)
