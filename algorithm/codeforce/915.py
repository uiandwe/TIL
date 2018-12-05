def solution(k, array):
    min_water = float('inf')
    for i in array:
        if k % i == 0:
            min_water = min(min_water, i)

    print(int(k/min_water))

solution(7, [1, 2, 3, 4, 5, 6, 7])
