def solution(k, a, array):

    d = []

    for i in array:
        cnt1 = k//(i[0]*a)
        cnt3 = (k-cnt1*i[0]*a) // a
        cnt2 = i[1]*(cnt1-1)
        d.append(cnt1*i[0]+cnt3+cnt2)

    print(d, min(d))


solution(100, 1, [[10, 5], [5, 10]])
solution(100, 2, [[30,30], [49,2], [50,50], [20,10]])

