
def solution(n, array):

    whiteKing = max(array[0]-1, array[1]-1)
    blackKing = max(n-array[0], n-array[1])

    if whiteKing == 0:
        print("w")
    elif blackKing == 0:
        print("b")
    elif whiteKing <= blackKing:
        print("w")
    else:
        print("b")

solution(4, [2, 3])
