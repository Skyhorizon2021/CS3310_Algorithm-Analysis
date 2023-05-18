#Name: Loc Nguyen
#Date: 05/16/2021
#Objective: Find kth smallest element using merge sort

import time

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

        i,j,k = 0
        
i,j,k = 0
print(i,j,k)