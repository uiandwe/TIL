# -*- coding: utf-8 -*-
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S, P, Q):
    dna_dict = {
        'A': 1,
        'C': 2,
        'G': 3,
        'T': 4
    }

    ret_array = []

    for p, q in zip(P, Q):
        temp_dna = S[p:q+1]
        ret_array.append(dna_dict[sorted(temp_dna)[0]])

    return ret_array

assert solution("CAGCCTA", [2, 5, 0], [4, 5, 6]) == [2, 4, 1]

