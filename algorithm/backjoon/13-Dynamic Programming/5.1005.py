import sys


d = [
    sys.maxint,
    sys.maxint,
    sys.maxint,
    sys.maxint,
    sys.maxint,
    sys.maxint,
    sys.maxint,
    sys.maxint
]

# edge = [
#     [],
#     [1],
#     [1],
#     [2],
#     [2],
#     [3],
#     [5, 6],
#     [7]
# ]
#
# value = [
#     10, 20, 1, 5, 8, 7, 1, 43
# ]


edge = [
    [],
    [1],
    [1],
    [2, 3]
]

value = [10, 1, 100, 10]

for index, array in enumerate(edge):
    if len(array) > 0:
        temp = []
        for i in array:
            temp.append(d[i-1]+value[index])
        d[index] = max(temp)
    else:
        if d[index] > value[index]:
            d[index] = value[index]

print d
