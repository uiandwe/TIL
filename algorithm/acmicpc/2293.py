def solution(coins, k):
    d = [0 for _ in range(k+1)]
    d[0] = 1
    for c in coins:
        for i in range(c, k+1):
            d[i] += d[i-c]

    print(d[k])


if __name__ == '__main__':
    nk_input = input()
    nk_input = nk_input.split(" ")
    n = int(nk_input[0])
    k = int(nk_input[1])

    coins = []
    for i in range(n):
        coins.append(int(input()))

    solution(coins, k)