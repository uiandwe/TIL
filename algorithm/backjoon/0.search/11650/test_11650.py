def solution(array):
    array = sorted(array, key=lambda x: x[1])
    return array


def test_11650():
    assert [[1, -1], [1, 1], [2, 2], [3, 3], [3, 4]] == solution([[3, 4], [1, 1], [1, -1], [2, 2], [3, 3]])
    assert [[1, -1], [1, 1], [3, 4]] == solution([[3, 4], [1, 1], [1, -1]])
