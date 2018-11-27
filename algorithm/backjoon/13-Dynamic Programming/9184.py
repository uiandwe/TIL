d = []

def solution(a, b, c):
    for i in range(21):
        temp1 = []
        for j in range(21):
            temp2 = []
            for k in range(21):
                temp2.append(0)
            temp1.append(temp2)
        d.append(temp1)
    print(backTrack(a, b, c))


def backTrack(a, b, c):
    if a<=20 and b <=20 and c <=20 and d[a][b][c] != 0:
        return d[a][b][c]

    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        d[20][20][20] = backTrack(20, 20, 20)
        return d[20][20][20]
    elif a < b and b < c:
        d[a][b][c] = backTrack(a, b, c-1) + backTrack(a, b-1, c-1) - backTrack(a, b-1, c)
        return d[a][b][c]
    else:
        d[a][b][c] = backTrack(a - 1, b, c) + backTrack(a - 1, b - 1, c) + backTrack(a - 1, b, c - 1) - backTrack(a - 1, b - 1,c - 1)
        return d[a][b][c]


solution(1, 1, 1)
solution(2, 2, 2)
solution(10, 4, 6)
solution(50, 50, 50)
solution(-1, 7, 18)
