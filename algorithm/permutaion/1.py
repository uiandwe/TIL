pick = []
array = []
def perm1(pos, m):
    if len(pick) == m:
        print(pick)
        return
    else:
        for i in range(pos, len(array)):
            pick.append(array[i])
            perm1(i+1, m)
            pick.pop()

def solution():
    global array
    array = [x+1 for x in range(3)]
    perm1(0, 3)


solution()
