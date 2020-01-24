"""
Remove minimum characters from both the strings to make the given strings anagram
Reference: https://www.hackerrank.com/challenges/ctci-making-anagrams/problem

Eg:
Enter first string: cddgk
Enter second string: gcd
2
"""


def make_anagram(a, b):
    char_arr = [0] * 26
    for char in a:
        char_arr[ord(char) - ord('a')] += 1
    for char in b:
        char_arr[ord(char) - ord('a')] -= 1

    return sum(map(abs, char_arr))


print(make_anagram(input("Enter first string: "), input("Enter second string: ")))
