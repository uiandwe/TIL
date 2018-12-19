def hat(n):

    if n <= 10:
        return n-1

    n -= 10
    index = 9
    evenNum = True
    start = 0

    while index < n:
        n -= index
        evenNum = not evenNum
        if evenNum is False:
            start += 1
            index = pow(10, start) * index

    retNum = 0

    if evenNum is True:
        temp = str(pow(10, start) + n-1)
        retNum = temp + temp[::-1]
    else:

        temp = str(pow(10, start + 1))
        mid = len(temp)//2

        temp = str((n - 1) + int(temp[:mid+1]))

        retNum = temp[:len(temp) - 1] + temp[len(temp)-1] + temp[:len(temp)-1][::-1]

    return retNum

def main():

    n = int(input())

    print(hat(n))

if __name__ == "__main__":
    main()
