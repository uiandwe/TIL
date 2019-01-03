


def test_solution():
    assert 2 == solution("}{")
    assert 0 == solution("{}{}{}")
    assert 1 == solution("{{{}")
    assert 0 == solution("{}{}")
    assert 2 == solution("{{{{")
