
def test_3184():
    map = [
        [".", ".", ".","#",".","."],
        [".", "#", "#","v","#","."],
        ["#", "v", ".","#",".","#"],
        ["#", ".", "o","#",".","#"],
        [".", "#", "#","#",".","#"],
        [".", ".", ".","#","#","#"]
    ]
    assert [0, 2] == solution(map)

    map = [
        [".",  "#","#","#","#","#","#","."],
        ["#", ".",".","o",".",".",".","#"],
        ["#", ".","#","#","#","#",".","#"],
        ["#", ".","#","v",".","#",".","#"],
        ["#", ".","#",".","o","#","o","#"],
        ["#", "o",".","#","#",".",".","#"],
        ["#", ".","v",".",".","v",".","#"],
        [".",  "#","#","#","#","#","#","."]
    ]

    assert [3, 1] == solution(map)
    
    
    map = [
        [".",  "#","#","#",".","#","#","#","#","#",".","."],
        ["#", ".","o","o","#",".",".",".","#","v","#","."],
        ["#", ".",".","o","#",".","#",".","#",".","#","."],
        ["#", ".",".","#","#","o","#",".",".",".","#","."],
        ["#", ".","#","v","#","o","#","#","#",".","#","."],
        ["#", ".",".","#","v","#",".",".",".",".","#","."],
        ["#", ".",".",".","v","#","v","#","#","#","#","."],
        [".",  "#","#","#","#",".","#","v","v",".","o","#"],
        [".",".",".",".",".",".",".",  "#","#","#","#","."]
    ]

    assert [3, 5] == solution(map)