# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, Y, D):
    share, remainder = (Y-X) // D, (Y-X)%D
    if remainder > 0:
        share += 1
    return share

assert solution(10, 85, 30) == 3

