'''
http://hellogohn.com/post_one318
'''

num1 = input()

def pre_premutation(x):
    str1 = str(x)
    strLen = len(str1)
    for i in range(strLen-1, 0, -1):
        if int(str1[i]) < int(str1[i-1]):
            tempArray1 = list(str1[:i])
            tempArray2 = list(str1[i:])
            print tempArray1, tempArray2

            tempArray1Len = len(tempArray1)
            tempArray2Len = len(tempArray2)
            templen = min(tempArray1Len, tempArray2Len)

            for j in range(templen):
                changeIntA = int(tempArray1[(tempArray1Len-1)-j])
                changeIntB = int(tempArray2[(tempArray2Len-1)-j])
                if changeIntA > changeIntB:
                    tempArray1[(tempArray1Len-1)-j] = str(changeIntB)
                    tempArray2[(tempArray2Len-1)-j] = str(changeIntA)
                    tempArray2.sort()
                    return ''.join(tempArray1)+''.join(tempArray2)


print pre_premutation(num1)
