'''
I(1), V(5), X(10), L(50), C(100), D(500), M(1000)

1 -> I
2 -> II
3 -> III
4 -> IV
7 -> VII
10 -> X
39 -> XXXIX
246 -> CCXLVI
207 -> CCVII
1066 -> MLXVI
1776 -> MDCCLXXVI
1954 -> MCMLIV
'''


def roman(n):
    dict = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }

    retStr = ''
    keys = list(dict.keys())
    values = list(dict.values())

    while n > 0:
        for index, key in enumerate(keys):
            if n >= key:
                retStr += values[index]
                n -= key
                break

    return retStr
