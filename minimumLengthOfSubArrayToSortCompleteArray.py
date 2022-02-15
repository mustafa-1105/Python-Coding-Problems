#Problem Statement: Find the length of minimum subarray to make the given array sorted
#https://www.ideserve.co.in/learn/minimum-length-subarray-sorting-which-results-in-sorted-array

def minSubArray(a):
    n = len(a)
    startIndex, endIndex = 0, n-1
    
    for i in range(n-1):
        if a[i] > a[i+1]:
            startIndex = i
            break
    
    #start, end, step
    for i in range(n-1, 0, -1):
        if a[i] < a[i-1]:
            endIndex = i
            break
        
    if startIndex != 0 and endIndex != n-1:    
        minElement = min(a[startIndex:endIndex+1])
        maxElement = max(a[startIndex:endIndex+1])
    else:
        minElement, maxElement = a[startIndex], a[endIndex]
    
    minIndex = findMinIndex(a, startIndex, minElement)
    maxIndex = findMaxIndex(a, endIndex, maxElement)

    print(minIndex)
    print(maxIndex)
    if minIndex == 0 and maxIndex == n-1:
        print(0)
    else:
        print(maxIndex-minIndex+1)
    
    return
    
def findMinIndex(a, startIndex, minElement):
    for i in range(startIndex):
        if(a[i] > minElement):
            return i
    return startIndex
    
def findMaxIndex(a, endIndex, maxElement):
    n = len(a)
    for i in range(n-1, endIndex-1, -1):
        if(a[i] < maxElement):
            return i
    return endIndex
    
a1 = [1, 2, 3, 4, 5]               
a3 = [1, 7, 6, 4, 5, 3, 11]
minSubArray(a1)

