def solution(strs, t):
    len_t = len(t)
    d = [float('inf') for x in range(len_t)]
    dict = {}
    for word in strs:
        dict[word] = 1

    d[len_t-1] = 0

    for i in range(len_t, -1, -1):
        tmp = ""
        for j in range(5):
            if i+j >= len_t-1:
                break

            tmp += t[i+j]
            if tmp in dict and tmp != strs[-1]:
                d[i] = min(d[i], d[i+j+1]+1)

    return d[0]
