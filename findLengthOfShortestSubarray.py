#Problem Solution: Shortest Subarray to be Removed to Make Array Sorted
#https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/
#https://www.geeksforgeeks.org/length-of-smallest-subarray-to-be-removed-such-that-the-remaining-array-is-sorted/

def findLengthOfShortestSubarray(self, a: List[int]) -> int:
    n = len(a)
    left, right = 0, n-1
    minLength = sys.maxsize
    start, end = -1, -1

    # Calculate the possible length of
    # the sorted subarray from left
    for i in range(n-1):
        if a[i] <= a[i+1]:
            left += 1
        else:
            break

    start, end = left+1, n-1
    #Array is sorted
    if left == n-1:
        return 0

    # Calculate the possible length of
    # the sorted subarray from left
    for i in range(right, left, -1):
        if a[i] >= a[i-1]:
            right -= 1
        else:
            break

    end = right

    minLength = min(n-left-1, right)

    # Calculate the possible length
    # in the middle we can delete
    # and update the result
    j = right
    for i in range(left+1):
        if a[i] <= a[j]:
            minLength = min(minLength, j-i-1)
        elif j < n-1:
            j += 1
        else:
            break
        start, end = i+1, j
    print(str(start) + " : " + str(end))

    return minLength
    
a1 = [1, 2, 3, 4, 5]          
a2 = [5, 10, 11, 8, 1]           
a3 = [1, 7, 6, 4, 5, 3, 11]
print(findLengthOfShortestSubarray(a2))
