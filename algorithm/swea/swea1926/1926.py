
def solution(n):
    ret_arr = [x for x in range(1, n+1)]

    for index, val in enumerate(ret_arr):
        str_dash = ''
        i = val
        while val > 0:
            remainder = val % 10
            val = val // 10
            if remainder != 0 and remainder % 3 == 0:
                str_dash += '-'
        if str_dash != '':
            ret_arr[index] = str_dash
        else:
            ret_arr[index] = i

    return ret_arr
