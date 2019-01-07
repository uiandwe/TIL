def solution(array):
    mulVal = 1
    d = [0 for i in range(10)]

    for i in array:
        mulVal *= i

    for i in str(mulVal):
        d[int(i)] += 1

    return d


def main():

    loop = int(input())
    data = []
    for i in range(loop):
        data.append(int(input()))

    for i in solution(data):
        print(i)

if __name__ == "__main__":
    main()

