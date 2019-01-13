def solution(array):
    dict = {}
    max_num = 0
    for num in array:
        max_num = max(max_num, num)
        if num in dict:
            return False
        else:
            dict[num] = num

    if len(array) == max_num:
        return True
    else:
        return False

