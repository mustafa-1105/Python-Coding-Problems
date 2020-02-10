"""
Problem Link: https://leetcode.com/problems/rotate-array/
"""

nums = [1, 2, 3, 4, 5, 6]
k = 7
n = len(nums)
k = k % n
if k != 0:
    nums = nums[-k:] + nums[:n - k]
print(nums)
