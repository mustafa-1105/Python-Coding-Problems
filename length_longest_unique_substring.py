"""
Length of the longest substring without repeating characters
Given a string str, find the length of the longest substring without repeating characters.

For “ABDEFGABEF”, the longest substring are “BDEFGA” and “DEFGAB”, with length 6.
"""

NUM_OF_CHARS = 256


def longest_unique_substring(string):
    max_len = 1
    cur_len = 1
    visited = [-1] * NUM_OF_CHARS
    visited[ord(string[0])] = 0

    for i in range(1, len(string)):
        prev_index = visited[ord(string[i])]
        if prev_index == -1 or (i - cur_len > prev_index):
            cur_len += 1
        else:
            if cur_len > max_len:
                max_len = cur_len
            cur_len = i - prev_index

        visited[ord(string[i])] = i

    if cur_len > max_len:
        max_len = cur_len

    return max_len


print(longest_unique_substring(str(input("Enter the string: "))))
