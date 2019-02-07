def solution(x):
    str_temp = str(x)
    temp = 0
    for c in str_temp:
        temp += int(c)

    if x % temp == 0:
        return True
    else:
        return False
