def test_1916():
    nodes = [
        [1, 2, 2],
        [1, 3, 3],
        [1, 4, 1],
        [1, 5, 10],
        [2, 4, 2],
        [3, 4, 1],
        [3, 5, 1],
        [4, 5, 3],
    ]

    start_node = 1
    end_node = 5
    node_count = 5
    assert 4 == solution(node_count, nodes, start_node, end_node)
