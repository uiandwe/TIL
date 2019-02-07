def solution(phone_number):

    star_len = len(phone_number[:-4])
    answer = ['*' for i in range(star_len)]

    return ''.join(answer) + phone_number[star_len:]
