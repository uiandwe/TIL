import sys
import math

def getMaxField(data, n, m) :
    map = [[0 for x in range(m)] for y in range(n)]

    for i in range(n):
        for j in range(m):
            if i > 0 and j > 0 and data[i][j] == 1 and data[i-1][j] == 1 and data[i][j-1] == 1 and data[i-1][j-1] == 1:
                if map[i-1][j-1] == map[i-1][j] == map[i][j-1]:
                    map[i][j] = pow(int(math.sqrt(map[i - 1][j - 1]))+1, 2)
                else:
                    map[i][j] = max(map[i-1][j-1],map[i-1][j],map[i][j-1])
            else:
                map[i][j] = data[i][j]

    retMax = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            if retMax < map[i][j]:
                retMax = map[i][j]

    return retMax

def main():
    '''
    이 부분은 수정하지 마세요.
    '''
    inputList = [int(x) for x in input().split()]
    
    n = inputList[0]
    m = inputList[1]
    data = [[int(x) for x in input().split()] for i in range(n)]

    print(getMaxField(data, n, m))

if __name__ == "__main__":
    main()
