dictionary = {}
d = []
str = ""



def lzw():
    global dictionary
    global d
    global str

    findStr = ""
    for i in range(1, len(str)+1):
        tempStr = str[0:i]

        if tempStr not in dictionary:
            findStr = tempStr
            break

    if len(str) <= 1:
        d.append(dictionary[str])
        return True

    dictionary[findStr] = len(dictionary)+1
    str = str[len(findStr)-1:]
    d.append(dictionary[findStr[:-1]])
    return lzw()


def solution(msg):
    global str

    str = msg
    for i in range(1, 27):
        dictionary[chr(64+i)] = i

    lzw()

    return d



print(solution("KAKAO"))
print([11, 1, 27, 15])
print(solution("TOBEORNOTTOBEORTOBEORNOT"))
print([20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34])
print(solution("ABABABABABABABAB"))
print([1, 2, 27, 29, 28, 31, 30])
