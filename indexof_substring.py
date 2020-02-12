"""
Find the index of first occurrence of the given string from another string
Problem Link: https://leetcode.com/problems/implement-strstr/
"""


def indexof_substring(haystack: str, needle: str) -> int:
    n = len(needle)
    h = len(haystack)
    if n < 1:
        return 0
    elif n > h:
        return -1

    i, j, temp = 0, 0, -1

    while i < h and h - i + 1 >= n:
        if haystack[i] == needle[j]:
            temp = i
            while j < n and i < h and haystack[i] == needle[j]:
                i += 1
                j += 1
            if j == n:
                return temp
            i = temp + 1
            j = 0
        else:
            i += 1

    return -1


print(str(indexof_substring('hello', 'll')))
