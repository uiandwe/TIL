def solution(v):
    point_x = 0
    point_y = 0

    for point in v:
        point_x ^= point[0]
        point_y ^= point[1]

    return [point_x, point_y]

