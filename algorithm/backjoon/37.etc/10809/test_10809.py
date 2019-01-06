def solution(str):
    d = [-1 for i in range(26)]
    for i in range(len(str)):
        position = ord(str[i])-97
        if d[position] == -1:
            d[position] = i
    return d


def test_10809():
    assert [1, 0, -1, -1, 2, -1, -1, -1, -1, 4, 3, -1, -1, 7, 5, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1] == solution("baekjoon")
    assert [0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1] == solution("aaaaaaaa")
    assert [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0] == solution("z")
