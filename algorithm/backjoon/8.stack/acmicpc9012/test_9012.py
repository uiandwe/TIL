def test_9012():
    vps = "(())())"
    assert "NO" == solution(vps)

    vps = "(((()())()"
    assert "NO" == solution(vps)

    vps = "(()())((()))"
    assert "YES" == solution(vps)

    vps = "((()()(()))(((())))()"
    assert "NO" == solution(vps)

    vps = "()()()()(()()())()"
    assert "YES" == solution(vps)

    vps = "(()((())()("
    assert "NO" == solution(vps)
