"""
Find index of 2 intergers whose sum is equal to the given number
Problem link: https://leetcode.com/problems/two-sum/
"""

nums = [2, 7, 11, 15]
target = 9

a = dict()
index = 0
for i in nums:
    diff = target - i
    if diff in a:
        print([index, a[diff]])
    a[i] = index
    index += 1
