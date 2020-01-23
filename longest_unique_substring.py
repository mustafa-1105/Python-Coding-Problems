"""
Print the longest substring without repeating characters
Given a string str, find the longest substring without repeating characters.

For “ABDEFGABEF”, the longest substring are “ABDEFG”, with length 6.
"""

NUM_OF_CHARS = 256


def longest_unique_substring(string):
    max_len = 1
    cur_len = 1
    visited = [-1] * NUM_OF_CHARS
    visited[ord(string[0])] = 0
    sub_str_start = 0
    start = 0

    for i in range(1, len(string)):
        prev_index = visited[ord(string[i])]
        if prev_index == -1 or (i - cur_len > prev_index):
            cur_len += 1
        else:
            cur_len = i - sub_str_start
            if cur_len > max_len:
                max_len = cur_len
                start = sub_str_start

            sub_str_start = prev_index + 1

        visited[ord(string[i])] = i

    if cur_len > max_len:
        max_len = cur_len
        start = sub_str_start

    return string[start: start + max_len]


print("Longest substring of given string is: " + longest_unique_substring(str(input("Enter the string: "))))
