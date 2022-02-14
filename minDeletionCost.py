# Problem Statement: 
# Given a string s and an array of integers cost where cost[i] is the cost of deleting the ith character in s.
# Return the minimum cost of deletions such that there are no two identical letters next to each other.
# Notice that you will delete the chosen characters at the same time, in other words, after deleting a character, the costs of deleting other characters will not change.

def minDeletionCost(s, cost):
    ans = 0
    groupSum = 0
    groupMax = 0
    
    for i in range(len(s)):
        if(i > 0 and s[i] != s[i-1]):
            ans += groupSum - groupMax
            groupSum = 0
            groupMax = 0
        
        
        groupMax = max(cost[i], groupMax)
        groupSum += cost[i] 
        
    
    # for last character
    ans += groupSum - groupMax
    return ans
    
s = "aaabbbabbbb"
cost = [3, 5, 10, 7, 5, 3, 5, 5, 4, 8, 1]
print(minDeletionCost(s, cost))
