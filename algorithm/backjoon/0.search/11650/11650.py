def solution(array):
    array = sorted(array, key=lambda x: x[1])
    return array
