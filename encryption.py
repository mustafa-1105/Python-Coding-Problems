"""
Encrypt the given string in a way mentioned here : https://www.hackerrank.com/challenges/encryption/problem

Eg:
Enter the string: haveaniceday
hae and via ecy
"""
import math


def encryption(s):
    n = len(s)
    len_sqrt = math.sqrt(n)
    cols = math.ceil(len_sqrt)
    rows = math.floor(len_sqrt)

    if (rows * cols) < n:
        rows += 1

    ret_str = ""
    for i in range(cols):
        for j in range(rows):
            index = i + (j * cols)
            if index < n:
                ret_str += s[index]
        ret_str += " "

    return ret_str


print(encryption(input("Enter the string: ")))
