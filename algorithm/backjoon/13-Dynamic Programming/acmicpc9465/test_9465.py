
def test_9465():
    stamp = [
        [50, 30]
    ]

    assert 50 == solution(stamp)

    stamp = [
        [100, 70],
        [20, 10],
        [40, 60]
    ]

    assert 160 == solution(stamp)

    stamp = [
        [50, 30],
        [10, 50],
        [100, 70],
        [20, 10],
        [40, 60]
    ]

    assert 260 == solution(stamp)

    stamp = [
        [10, 20],
        [30, 40],
        [10, 30],
        [50, 50],
        [100, 60],
        [20, 20],
        [40, 80]
    ]

    assert 290 == solution(stamp)
