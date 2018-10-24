import sys

a = []

for i in range(8):
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
        print a[x][y]
        return
    else:
        sys.stdout.write("(")
        m = n//2
        for i in range(2):
            for j in range(2):
                solve(x+i*m, y+j*m, m)
        sys.stdout.write(")")

solve(0, 0, 8)


