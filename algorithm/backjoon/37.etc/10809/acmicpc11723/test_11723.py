
def test_11723():
    input_op = [
        ["add",  1],
        ["add", 2],
        ["check", 1],
        ["check", 2],
        ["check", 3],
    ]
    assert [1, 1, 0] == solution(input_op)

    input_op = [
        ["add", 1],
        ["add", 2],
        ["check", 1],
        ["check", 2],
        ["check", 3],
        ["remove", 2],
        ["check", 1],
        ["check", 2]
    ]
    assert [1, 1, 0, 1, 0] == solution(input_op)

    input_op = [
        ["add", 1],
        ["add", 2],
        ["check", 1],
        ["check", 2],
        ["check", 3],
        ["remove", 2],
        ["check", 1],
        ["check", 2],
        ["toggle", 3],
        ["check", 1],
        ["check", 2],
        ["check", 3],
        ["check", 4]
    ]
    assert [1, 1, 0, 1, 0, 1, 0, 1, 0] == solution(input_op)

    input_op = [
        ["add", 1],
        ["add", 2],
        ["check", 1],
        ["check", 2],
        ["check", 3],
        ["remove", 2],
        ["check", 1],
        ["check", 2],
        ["toggle", 3],
        ["check", 1],
        ["check", 2],
        ["check", 3],
        ["check", 4],
        ["all"],
        ["check", 10],
        ["check", 20]
    ]
    assert [1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1] == solution(input_op)
