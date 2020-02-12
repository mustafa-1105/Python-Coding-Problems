import operator

list1 = [[1234, 5], [234, 6], [2354, 7]]
list2 = [[1234, 5], [234, 6], [458, 6], [2354, 7]]

r = list()
for x in list2:
    if x not in list1:
        r.append(x)
r.sort(key=operator.itemgetter(1))

a = []
for i in r:
    a.append(i[0])
print(a)
