def test_4():
    board = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
    assert 9 == solution(board)

    board = [[0,0,1,1],[1,1,1,1]]
    assert 4 == solution(board)
