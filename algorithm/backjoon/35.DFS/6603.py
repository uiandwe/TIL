lotte = []

def dfs(array, node):
    global lotte

    if len(array) == 6:
        print(array)
        return
    else:
        for i in range(node, len(lotte)):
            array.append(lotte[i])
            dfs(array, i+1)
            array.pop()

def solution(array):
    global lotte
    lotte = array

    dfs([], 0)

solution([1, 2, 3,4 ,5 ,6, 7])
solution([1, 2, 3, 5, 8, 13, 21, 34])
