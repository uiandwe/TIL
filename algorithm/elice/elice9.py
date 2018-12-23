def changeNToM(n, m):
    arr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    retArr = []

    while True:
        remainder = n % m
        n /= m
        retArr.append(arr[int(remainder)])
        if n < m:
            retArr.append(arr[int(n)])
            break

    return ''.join(reversed(retArr))

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    n = int(input())
    m = int(input())

    print(changeNToM(n, m))

if __name__ == "__main__":
    main()
