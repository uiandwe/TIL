'''
1 -> 0
2 -> 3
3 -> 5
4 -> 11
5 -> 21

d[i] = d[i-1] + d[i-2]*2
'''


def solution(n):

    if n == 1:
        return 0
    if n == 2:
        return 3
    if n == 3:
        return 5

    d = [0 for x in range(n+1)]

    d[1] = 0
    d[2] = 3
    d[3] = 5

    for i in range(4, n+1):
        d[i] = d[i-1] + (d[i-2]*2)
    return d[n]


def test_1793():
    assert 3 == solution(2)
    assert 171 == solution(8)
    assert 2731 == solution(12)
    assert 845100400152152934331135470251 == solution(100)
    assert 1071292029505993517027974728227441735014801995855195223534251 == solution(200)
