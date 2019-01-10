
def test_1967():
    n = 12
    node_array = [
        [1, 2, 3],
        [1, 3, 2],
        [2, 4, 5],
        [3, 5, 11],
        [3, 6, 9],
        [4, 7, 1],
        [4, 8, 7],
        [5, 9, 15],
        [5, 10, 4],
        [6, 11, 6],
        [6, 12, 10]
    ]
    assert 45 == solution(n, node_array)

    n = 5
    node_array = [
        [1, 2, 1],
        [1, 3, 1],
        [2, 4, 2],
        [3, 5, 4]
    ]
    assert 8 == solution(n, node_array)

    n = 7
    node_array = [
        [1, 2, 1],
        [1, 3, 1],
        [2, 4, 2],
        [2, 5, 10],
        [3, 6, 5],
        [3, 7, 4],
    ]
    assert 17 == solution(n, node_array)
