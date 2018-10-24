a = []
cnt = [0, 0, 0]

for i in range(9):
    str = raw_input()
    str = str.split(" ")

    temp = []
    for j in str:
        temp.append(int(j))

    a.append(temp)


def same(x, y, n):
    for i in range(x, x+n):
        for j in range(y, y+n):
            if a[x][y] != a[i][j]:
                return False

    return True


def solve(x, y, n):
    if same(x, y, n) is True:
        cnt[a[x][y]+1] += 1
        return

    m = n//3
    for i in range(3):
        for j in range(3):
            solve(x+i*m, y+j*m, m)


solve(0, 0, 9)
print cnt
