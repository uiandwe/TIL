
def test_380():
    rs = RandomizedSet()
    assert True is rs.insert(1)
    assert False is rs.remove(2)
    assert True is rs.insert(2)
    r = rs.getRandom()
    assert (1 == r or 2 == r)
    assert True is rs.remove(1)
    assert False is rs.insert(2)
    assert 2 == rs.getRandom()
