import itertools

pool = [0, 1, 7]

arr = []
for i in range(1, len(pool)+1):
    for values in list(itertools.permutations(pool, i)):
        arr.append(int(''.join([str(i) for i in values])))


print(list(set(arr)))



