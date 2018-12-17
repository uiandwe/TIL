def checkAlphabat(str):
    retArr = []
    for c in str:
        if c.isalpha():
            retArr.append(c)

    return retArr


def intToArr(index, checkLen):
    int_list = []
    for i in str(index):
        int_list.append(i)

    if len(int_list) < checkLen:
        int_list = ['0'] + int_list

    return int_list


def checkDuplication(arr):
    temp_list = []
    for i in arr:
        if i in temp_list:
            return False
        else:
            temp_list.append(i)

    return True


def changeCharToInt(str, alphabat, intList):
    retStr = ""

    for c in str:
        if c.isalpha():
            retStr += intList[alphabat.index(c)]
        else:
            retStr += c
    return int(retStr)


def solution(p, q, r):

    alphabat = []
    alphabat += checkAlphabat(p)
    alphabat += checkAlphabat(q)
    alphabat += checkAlphabat(r)
    alphabat = sorted(list(set(alphabat)))

    print(alphabat)
    intLen = len(alphabat)
    index = pow(10, intLen-2)
    end = pow(10, intLen)

    ret_array = []
    while index < end:
        int_list = intToArr(index, intLen)

        next_step = checkDuplication(int_list)

        if next_step is True:
            temp_p = changeCharToInt(p, alphabat, int_list)
            temp_q = changeCharToInt(q, alphabat, int_list)
            temp_r = changeCharToInt(r, alphabat, int_list)

            if temp_p + temp_q == temp_r:
                ret_array.append((temp_p, temp_q, temp_r))

        index += 1

    print(ret_array)


solution("AA", "BC", "100")
solution("XYZ", "XY", "6PP")
