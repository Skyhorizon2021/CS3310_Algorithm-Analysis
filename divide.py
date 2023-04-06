#Name: Loc Nguyen
#CS3310 Project 1
import random,time, numpy as np


size = 2048


#function to split matrix into quarters
def split(matrix):
    """
    Splits a given matrix into quarters.
    Input: nxn matrix
    Output: tuple containing 4 n/2 x n/2 matrices corresponding to a, b, c, d
    """
    #row, col = matrix.shape
    #row2, col2 = row//2, col//2
    #return matrix[:row2, :col2], matrix[:row2, col2:], matrix[row2:, :col2], matrix[row2:, col2:]
    upperhalf = np.hsplit(np.vsplit(matrix, 2)[0],2)
    lowerhalf = np.hsplit(np.vsplit(matrix, 2)[1],2)
    
    upperleft = upperhalf[0]
    upperright = upperhalf[1]
    lowerleft = lowerhalf[0]
    lowerright = lowerhalf[1]
    
    return upperleft,upperright,lowerleft,lowerright

#function to print out matrix
def printMatrix(matrix, row, col):
    for i in range(row):
        for j in range(col):
            print(matrix[i][j], end = " ")
        print()
    print()

            
#function to multiply matrix
def multiply(matrixA, matrixB):
    col1 = len(matrixA[0])
    row2 = len(matrixB)
    
    #edge cases
    if (col1 != row2):
        print("\nError: The number of columns in Matrix A must be equal to the number of rows in Matrix B\n")
        return 0
    if (col1 == 1):
        return matrixA[0][0]*matrixB[0][0]
    else:
        a, b, c, d = split(matrixA)
        e, f, g, h = split(matrixB)

        #perform addition of products
        matrixC11=multiply(a,e) + multiply(b,g)
        matrixC12=multiply(a,f) + multiply(b,h)
        matrixC21=multiply(c,e) + multiply(d,g)
        matrixC22=multiply(c,f) + multiply(d,h)            
    
        # Combining the 4 quadrants into a single matrix by stacking horizontally and vertically.
        matrixC = np.vstack((np.hstack((matrixC11, matrixC12)), np.hstack((matrixC21, matrixC22))))

        return matrixC
#initialize matrices with random number from 0 to 9 and matrixC with 0 then print out matrix for validation            
trialTime = []
for i in range(10):
    print("Trial",i+1)
    start = time.time()        
    #print("Matrix A")
    matrixA = np.array([[random.randint(0,9) for x in range(size)]for y in range (size)])
    #printMatrix(matrixA,size,size)
    #print("Matrix B")
    matrixB = np.array([[random.randint(0,9) for x in range(size)]for y in range (size)])
    #printMatrix(matrixB,size,size)           
    #print("Matrix C")
    #printMatrix(multiply(matrixA,matrixB),size,size)
    #end of algo            
    end = time.time()
    executionTime = end-start
    #print(executionTime)
    trialTime.append(executionTime)
#sort to find worst and best time to compute average time
trialTime.sort()
averageTime = (sum(trialTime)-trialTime[0] - trialTime[len(trialTime)-1])/(8)
print("Average time is %.5f" % averageTime)