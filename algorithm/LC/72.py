def solution(word1, word2):
    len1 = len(word1)
    len2 = len(word2)

    d = []

    for i in range(len1+1):
        temp = []
        for j in range(len2+1):
            temp.append(0)
        d.append(temp)

    for i in range(len(d)):
        d[i][0] = i
    for j in range(len(d[0])):
        d[0][j] = j

    for i in range(1, len1+1):
        for j in range(1, len2+1):
            if word1[i-1] == word2[j-1]:
                d[i][j] = d[i-1][j-1]
            else:
                d[i][j] = min(d[i-1][j-1], d[i-1][j], d[i][j-1])+1

    for i in d:
        print(i)


solution("horse", 'ros')
solution("intention", 'execution')
