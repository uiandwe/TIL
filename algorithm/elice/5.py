import sys

def getSubsum(data) :
    '''
    n개의 숫자가 list로 주어질 때, 그 연속 부분 최대합을 반환하는 함수를 작성하세요.
    '''

    d = [0 for x in data]
    d[0] = data[0]

    for i in range(1, len(data)):
        if d[i-1]+ data[i] <= 0:
            d[i] = 0
        else:
            d[i] = max(d[i-1] + data[i], data[i])
    return max(d)

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    # data = [int(x) for x in input().split()]

    print(getSubsum([1, 2, -4, 5, 3, -2, 9, -10]))

if __name__ == "__main__":
    main()
