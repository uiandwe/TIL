dwarf = []

def dfs(array, node):

    if len(array) == 7:
        if sum(array) == 100:
            print(array)
        return
    else:
        for i in range(node, len(dwarf)):
            array.append(dwarf[i])
            dfs(array, i+1)
            array.pop()


def solution(array):
    global dwarf
    dwarf = sorted(array)

    dfs([], 0)

solution([20,
7,
23,
19,
10,
15,
25,
8,
13])
