def solution(moves):
    if moves.count("U") == moves.count("D") \
            and moves.count("L") == moves.count("R"):
        return True
    else:
        return False
