def test_2156():
    arr = [6, 10]
    assert 16 == solution(arr)

    arr = [6, 10, 13]
    assert 23 == solution(arr)

    arr = [6, 10, 13, 9, 8, 1]
    assert 33 == solution(arr)

    arr = [6, 10, 13, 1, 20]
    assert 43 == solution(arr)
