#Name: Loc Nguyen
#Date: 05/16/2021
#Objective: Find kth smallest element using quick sort

import time
import random

arraySize = 2**19
k = 2

def quickSort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = random.choice(array)
        leftArr = [x for x in array[1:] if x < pivot]
        rightArr = [x for x in array[1:] if x >= pivot]
        return quickSort(leftArr) + [pivot] + quickSort(rightArr)

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
    
    sortedArray = quickSort(inputArray)
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