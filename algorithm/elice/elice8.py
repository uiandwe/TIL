def q(arr):

    if len(arr) <= 1:
        return arr

    equal = []
    more = []
    less = []
    pivot = len(arr) // 2

    for i in arr:
        if i == arr[pivot]:
            equal.append(i)
        elif i > arr[pivot]:
            more.append(i)
        else:
            less.append(i)
    return q(less) + equal + q(more)

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    n = int(input())
    data = [int(x) for x in input().split()]

    print(" ".join(str(x) for x in q(data)))

if __name__ == "__main__":
    main()
