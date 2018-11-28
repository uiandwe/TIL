def valid(mid, array, total):
    ret = 0
    for i in array:
        ret += min(mid, i)
    return ret <= total


def solution(t, array):

    right = t
    left = 0

    while left != right:
        mid = int((left + right + 1) / 2)
        if valid(mid, array, t):
            left = mid
        else:
            right = mid - 1

    print(left)


solution(201, [90, 150])
solution(485, [120,110,140,150])
