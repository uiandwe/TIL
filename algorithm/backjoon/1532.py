def solution(array1, array2):
    if array1[0] < array2[0]: #금화가 적다면 은화를 금화로 바꿈
        plusG = array2[0] - array1[0]
        array1[1] -= plusG * 11
        array1[0] += plusG
    else:
        miunsG = array1[0] - array2[0]
        array1[0] -= miunsG
        array1[1] += miunsG * 9

    if array1[1] < array2[1]:
        plugS = array2[1] - array1[1]
        array1[2] -= plugS * 11
        array1[1] += plugS
    else:
        minusS = array1[1] - array2[1]
        array1[1] -= minusS
        array1[2] += minusS * 9

    while True:
        print(array1, array2)
        if array1 == array2:
            break
        elif array1[1] < array2[1] and array1[2] < array2[2]:
            break
        else:
            if array1[1] != array2[1]:
                if array1[1] < array2[1]:
                    array1[1] += 1
                    array1[2] -= 11
                else:
                    array1[1] -= 1
                    array1[2] += 9
            else:
                if array1[2] < array2[2]:
                    array1[1] += 9
                    array1[2] -= 1
                else:
                    array1[1] += 1
                    array1[2] -=  11





solution([1, 100, 12], [5, 53, 33])
