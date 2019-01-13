def test_1():
    strs = ["ba", "na", "n", "a"]
    t = "banana"
    assert 3 == solution(strs, t)

    strs = ["app", "ap", "p", "l", "e", "ple", "pp"]
    t = "apple"
    assert 2 == solution(strs, t)

    strs = ["ba","an","nan","ban","n"]
    t = "banana"
    assert -1 == solution(strs, t)
