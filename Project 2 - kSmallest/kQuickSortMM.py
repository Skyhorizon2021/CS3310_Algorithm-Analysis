#Name: Loc Nguyen
#Date: 05/16/2021
#Objective: Find kth smallest element using quick sort median of median

import time
import random
import math

arraySize = 2**19
k = 2
#function to find median
def findMedian(a, p, r):
    L = []
    for i in range(p, r+1):
        L.append(a[i])
    L.sort()
    return L[(r-p+1)//2]

    
def quickSortMM(array):
    if len(array) <= 1:
        return array
    else:
        pivot = findMedian(array,0,len(array)-1)
        leftArr = [x for x in array[1:] if x < pivot]
        rightArr = [x for x in array[1:] if x >= pivot]
        return quickSortMM(leftArr) + [pivot] + quickSortMM(rightArr)

#generate array size for test cases
def inputGenerator(size):
    array = [random.randint(0,size*10) for i in range(arraySize)]
    return array
trialTime = []
for i in range(10):
    print("Trial",i+1)
    start = time.time()
    
    inputArray = inputGenerator(arraySize)
    #print("Input Array:",inputArray)
    
    sortedArray = quickSortMM(inputArray)
    #print("Sorted Array:",sortedArray)
    print("The kth ( k =",k,") smallest element:",sortedArray[k-1])
    #end of algorithm
    end = time.time()
    executionTime = end - start
    trialTime.append(executionTime)

#sort to find worst and best time to compute average time
trialTime.sort()
averageTime = (sum(trialTime)-trialTime[0] - trialTime[len(trialTime)-1])/(8)
print("Average time is %.5f" % averageTime)