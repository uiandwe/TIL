
def test_1238():
    nodes = [
        [1, 2, 4],
        [1, 3, 2],
        [1, 4, 7],
        [2, 1, 1],
        [2, 3, 5],
        [3, 1, 2],
        [3, 4, 4],
        [4, 2, 3]
    ]
    len_node = 4
    end_node = 2
    assert 10 == solution(len_node, nodes, end_node)
