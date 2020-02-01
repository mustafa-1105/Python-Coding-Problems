"""
Sort the given array in the format given here  https://www.hackerrank.com/challenges/countingsort4/problem
"""


def count_sort(arr):
    n = len(arr)
    values = [[]] * n
    i = 0
    for x in arr:
        index = int(x[0])

        if i < n / 2:
            if not values[index]:
                values[index] = '- '
            else:
                values[index] += '- '
        else:
            if not values[index]:
                values[index] = (x[1] + ' ')
            else:
                values[index] += (x[1] + ' ')

        i += 1

    s = ''
    for x in values:
        if x:
            s += x
    print(s)


n = int(input('Enter the size of array: '))
print('Enter array values: ')
arr = list()
for i in range(n):
    arr.append(input().rstrip().split())

count_sort(arr)
