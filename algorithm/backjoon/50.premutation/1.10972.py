'''
http://kwanghyuk.tistory.com/25
'''
num1 = input()

def next_premutation(x):
    str1 = str(x)
    strLen = len(str1)
    for i in range(strLen-1, 0, -1):
        if int(str1[i]) > int(str1[i-1]):
            tempArray1 = list(str1[:i])
            tempArray2 = list(str1[i:])

            tempArray1Len = len(tempArray1)
            tempArray2Len = len(tempArray2)
            templen = max(tempArray1Len, tempArray2Len)

            for j in range(templen):
                changeIntA = 0
                if j > tempArray1Len:
                    changeIntA = int(tempArray1[(tempArray1Len-1)])
                else:
                    changeIntA = int(tempArray1[(tempArray1Len-1)-j])

                changeIntB = 0
                if j > tempArray2Len:
                    changeIntB = int(tempArray2[(tempArray2Len-1)])
                else:
                    changeIntB = int(tempArray2[(tempArray2Len-1)-j])

                if changeIntA < changeIntB:
                    if j > tempArray1Len:
                        tempArray1[(tempArray1Len-1)] = str(changeIntB)
                    else:
                        tempArray1[(tempArray1Len-1)-j] = str(changeIntB)

                    if j > tempArray2Len:
                        tempArray2[(tempArray2Len-1)] = str(changeIntA)
                    else:
                        tempArray2[(tempArray2Len-1)-j] = str(changeIntA)

                    tempArray2.sort()
                    return ''.join(tempArray1)+''.join(tempArray2)


print next_premutation(num1)
