#Name: Loc Nguyen
#Date: 05/16/2021
#Objective: Find kth smallest element using merge sort

import time
import random

arraySize = 2**19
k = 2
#define merge sort function
def mergeSort(array):
    #check length of array
    if len(array) > 1:
        divider = len(array)//2
        leftArr = array[:divider]
        rightArr = array[divider:]
        #recursively call merge sort
        mergeSort(leftArr)
        mergeSort(rightArr)

        i,j,k = 0,0,0
        
        #check length is greater than 0
        while i < len(leftArr) and j < len(rightArr):
            #compare left and right, find smaller element and replace it
            if leftArr[i] < rightArr[j]:
                array[k] = leftArr[i]
                i += 1
            else:
                array[k] = rightArr[j]
                j += 1
            k += 1
        #taking care of leftover elements
        while i < len(leftArr):
            array[k] = leftArr[i]
            i+= 1
            k+= 1
        
        while j < len(rightArr):
            array[k] = rightArr[j]
            j += 1
            k += 1
    return array

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
    sortedArray = mergeSort(inputArray)

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