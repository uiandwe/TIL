
def test_2210():
    map = [
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 2, 1],
        [1, 1, 1, 1, 1]
    ]

    assert 15 == solution(map)
