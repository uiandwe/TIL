def solution(str):
    d = [-1 for i in range(26)]
    for i in range(len(str)):
        position = ord(str[i])-97
        if d[position] == -1:
            d[position] = i
    return d
