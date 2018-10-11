def splitArrayby2(str):
    array = []
    str = str.lower()
    for i in range(len(str)):
        if i+1 < len(str):
            tempStr = str[i]+str[i+1]
            if tempStr.isalpha() is True:
                array.append(tempStr)
    return array


def arrayToDict(array):
    dict = {}
    for i in array:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict

def intersection(dict1, dict2):
    intersectionCount = 0
    for i in dict1:
        if i in dict2:
            intersectionCount += min(dict1[i], dict2[i])
    return intersectionCount


def union(dict1, dict2):
    unioncount = 0
    tempDict = dict1
    for i in dict2:
        if i in tempDict:
            tempDict[i] = max(tempDict[i], dict2[i])
        else:
            tempDict[i] = dict2[i]

    for i in tempDict:
        unioncount += tempDict[i]
    return unioncount


def solution(str1, str2):

    strArray1 = splitArrayby2(str1)
    strArray2 = splitArrayby2(str2)

    strDict1 = arrayToDict(strArray1)
    strDict2 = arrayToDict(strArray2)

    intersectionCount = intersection(strDict1, strDict2)
    unionCount = union(strDict1, strDict2)

    if intersectionCount == 0 and unionCount == 0:
        intersectionCount = 1
        unionCount = 1
    answer = (intersectionCount/(unionCount*1.0))

    # print(intersectionCount, unionCount, answer, int(answer*65536))

    return int(answer*65536)


print(solution("FRANCE", "french"))
print(solution("handshake", "shake hands"))
print(solution("aa1+aa2", "AAAA12"))
print(solution("E=M*C^2", "e=m*c^2"))






