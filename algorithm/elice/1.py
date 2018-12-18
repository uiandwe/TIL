def findKth(myInput, k) :
    '''
    매 순간마다 k번째로 작은 원소를 리스트로 반환합니다.
    '''

    result = []
    for i in range(len(myInput)):
        temp_arr = myInput[:i+1]
        if len(temp_arr) >= k:
            temp_arr = sorted(temp_arr)
            result.append(temp_arr[k-1])
        else:
            result.append(-1)
    return result

def main():
    '''
    테스트를 하고싶으면, 아래 부분을 수정합니다.
    '''

    firstLine = [int(x) for x in input().split()]
    myInput = [int(x) for x in input().split()]

    print(*findKth(myInput, firstLine[1]))
if __name__ == "__main__":
    main()
