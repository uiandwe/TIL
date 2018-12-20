import sys

def LIS(arr):
    d = [1 for x in arr]

    for i in range(len(arr)):
        for j in range(0, i+1):
            if arr[i] > arr[j] and d[i] < d[j] + 1:
                d[i] = d[j]+1

    return max(d)

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    temp = [int(x) for x in input().split()]


    print(LIS(temp))

if __name__ == "__main__":
    main()
