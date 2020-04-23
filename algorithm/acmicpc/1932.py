"""
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
"""

def solution(n, array):
    d = [[0 for _ in range(n)] for _ in range(n)]
    d[0][0] = array[0][0]
    answer = 0

    for y in range(1, n):
        for x in range(n):
            if x == 0:
                d[y][x] = d[y-1][x] + array[y][x]
            else:
                d[y][x] = max(d[y-1][x-1], d[y-1][x]) + array[y][x]

        answer = max(answer, max(d[y]))

    print(answer)



n = int(input())
array = []
for i in range(n):
    temp = input()
    temp = list(map(int, temp.split(" ")))
    while len(temp) < n:
        temp.append(0)
    array.append(temp)

solution(n, array)