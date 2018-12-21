def solve(n):
    '''
    n개의 컵케이크를 3개짜리 봉지와 5개짜리 봉지만을 사용하여 포장할 때
    필요한 봉지의 최소 개수를 반환하는 함수를 작성하세요.
    컵케이크를 정확히 포장할 수 없을 때는 -1을 반환하세요.
    '''

    if (n-3) % 5 != 0 and (n-5) % 3 != 0:
        return -1

    d = [float('inf') for x in range(n + 1)]
    d[0] = 0

    for i in [3, 5]:
        for j in range(i, n+1):
            if d[j] > d[j-i]+1:
                d[j] = d[j-i]+1

    if d[n] == float('inf'):
        return -1
    else:
        return d[n]


def main():
    '''
    테스트를 하고싶으면, 아래 부분을 수정합니다.
    '''

    n = int(input())
    print(solve(n))


if __name__ == "__main__":
    main()
