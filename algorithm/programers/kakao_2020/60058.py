def is_right(p):
    count = 0
    for i, j in enumerate(p):
        if j == '(':
            count += 1
        else:
            count -= 1
        if count == -1:
            return False
    return True


def solution(p):
    if p == '' or is_right(p):
        return p

    count = 0

    for i, j in enumerate(p):
        if j == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            if p[0] == '(':
                return p[:i+1]+solution(p[i+1:])
            else:
                temp = ""
                for c in p[:i+1][1:][:-1]:
                    if c == "(":
                        temp += ")"
                    else:
                        temp += "("
                return '('+solution(p[i+1:])+')'+temp


print(solution("()))((()"))
