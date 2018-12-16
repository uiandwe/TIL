'''
1. for a를 순회하면서
2. sort(a[i] + b)로 b에 a원소를 집어 넣은 리스트 temp 생성 (getNeighbor())
3. temp에서 a[i]를 중심으로 3개를 뽑아냅 [b1, a[i], b2](getNeighbor())
4. b1, b2값이 없을 경우 -1로 대체  (set3SizeArr())
5. atob 리스트 생성 
5. C도 2번~4번 과정 -> atoc 리스트 생성
6. atob, atoc로 이중 배열 생성
[[b1, a, b2]
[c1, a, c2]]
7. a, b, c의 모두 사이값이 정해졌으므로 해당 배열에서의 경우의 수에 따른 min값을 추출 (getMinVal())
   경우의 수는 a < b < c  -> [0][1], [0][2], [1][2]
            b < a < c  -> [0][0], [0][1], [1][2]
            b < c < a  -> [0][0], [1][0], [1][1]
            c < b < a  -> [1][0], [1][1], [0][2]
8. 1번까지를 반복 하며 가장 작은 min을 찾음
'''


def getNeighbor(array, n):
    temp = [n] + array
    temp = sorted(temp)

    aIndex = temp.index(n)
    start = aIndex - 1
    start = 0 if start < 0 else start
    end = aIndex + 2

    return temp[start:end]


def set3SizeArr(arr, n):
    nIndex = arr.index(n)
    if nIndex == 0:
        arr = [-1]+arr
    elif len(arr) == 2:
        arr = arr+[-1]
    return arr


def retMin(a, b, c):
    return max([a, b, c]) - min([a, b, c])


def getMinVal(arr1, arr2):

    temp = [arr1, arr2]
    min_arr = [float('inf')]
    if temp[0][0] != -1 and temp[1][2] != -1:
        min_arr.append(retMin(temp[0][0], temp[0][1], temp[1][2]))
    if temp[0][2] != -1 and temp[1][2] != -1:
        min_arr.append(retMin(temp[0][1], temp[0][2], temp[1][2]))
    if temp[0][0] != -1 and temp[1][0] != -1:
        min_arr.append(retMin(temp[0][0], temp[1][0], temp[1][1]))
    if temp[1][0] != -1 and temp[0][2] != -1:
        min_arr.append(retMin(temp[1][0], temp[1][1], temp[0][2]))

    return min(min_arr)

def solution():
    a = [1, 18, 30, 44, 58]
    b = [23, 50, 60]
    c = [35, 42, 45, 63]

    minVal = float('inf')
    for i in range(len(a)):
        atob = getNeighbor(b, a[i])
        atoc = getNeighbor(c, a[i])

        atob = set3SizeArr(atob, a[i])
        atoc = set3SizeArr(atoc, a[i])

        tempMinVal = getMinVal(atob, atoc)
        if minVal > tempMinVal:
            minVal = tempMinVal

    print(minVal)


solution()
