import sys

#Problem statement:
# An array A consisting of N integers is given. The elements of array A together represent a chain, and each element represents the strength of each link in the chain. We want to divide this chain into three smaller chains. All we can do is break the chain in exactly two non-adjacent positions. More precisely, we should break links P,Q (0 < P < Q < N - 1, Q - P > 1), resulting in three chains [0, P - 1], [P   1, Q - 1], [Q   1, N - 1]. The total cost of this operation is equal to A[P]   A[Q].

def chain(a):
    prevBest = 1
    totalCost = sys.maxsize
    
    for i in range(3, a.length -1):
        if(a[i-2] < a[prevBest]):
            prevBest = i-2
        
        currCost = a[prevBest] + a[i]
        if(totalCost > currCost):
            totalCost = currCost
    
    return totalCost
    
a = [5, 2, 4, 6, 3, 7]

print(chain(a))
