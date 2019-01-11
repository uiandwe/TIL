
def test_12865():
    backpack = [
        [6, 13],
        [4, 8],
        [3, 6],
        [5, 12]
    ]
    max_weight = 7

    assert 14 == solution(max_weight, backpack)
