
def test_binary_searcy():
    input_a = [i for i in range(100)]
    target = 55
    expected = 55
    assert expected == bs(input_a, target)

    input_a2 = [i ** 2 for i in range(10)]
    target2 = 81
    expected2 = 9
    assert expected2 == bs(input_a2, target2)

    input_a3 = [i ** 2 for i in range(10)]
    target3 = -81
    expected3 = -1
    assert expected3 == bs(input_a3, target3)
