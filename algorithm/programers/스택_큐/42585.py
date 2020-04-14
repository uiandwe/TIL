def solution(arrangement):
    answer = 0
    s = []
    for index, val in enumerate(arrangement):
        if val == "(":
            s.append("(")
            answer += 1
        else:
            # 레이저
            if arrangement[index-1] == "(":
                answer += (len(s)-1) -1
            s.pop()

    return answer


assert solution("()(((()())(())()))(())") == 17
assert solution("()") == 0
assert solution("(())") == 2
assert solution("((()))") == 4
assert solution("(((())))") == 6
assert solution("(()())") == 3
assert solution("((()()))") == 6
assert solution("(((()())))") == 9
