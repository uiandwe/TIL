def solution(N, stages):
    answer = []
    test = []

    for i in range(0, N+1):
        test.append(0)

    totalSuccess = 0

    for s in stages:
        if s == 1:
            test[s] +=1
        elif s > N:
            totalSuccess += 1
            test[s-1] += 1
        else:
            test[s] += 1

    add = 0
    sortObj = {}

    for key in range(N, 0, -1):
        success = 0
        ing = 0
        failRate = 0

        if key == N:
            add += test[key]
            success = totalSuccess
            ing = test[key]
        else:
            success = add
            add += test[key]
            ing = add

        if ing != 0:
            failRate = success / ing

        if failRate in sortObj:
            sortObj[failRate].append(key)
        else:
            sortObj[failRate] = [key]

    for i in sorted(sortObj.keys()):
        answer += sorted(sortObj[i])

    return answer


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(3, [4, 4, 4, 4, 4]))
import random
n = random.randrange(1, 500)
a = []
for i in range(1, 200000):
    a.append(random.randrange(0, n))

print(solution(n, a))
