def solution(arr):
    dict = {}
    for word in arr:
        hash_key = get_key(word.lower())
        if hash_key in dict:
            dict[hash_key] += 1
        else:
            dict[hash_key] = 1

    return dict


def get_key(str):
    key = 0
    p = 1
    pn = 23
    hashSize = 5
    for c in str:
        key += ord(c) * p
        p *= pn
    return key % hashSize


def test_1():
    words = ["lucy",
            "lucid",
            "pure",
            "purity",
            "seraphic",
            "bijou",
            "melody",
            "iris",
            "lovable"
            ]
    assert {2: 2, 0: 2, 1: 2, 3: 2, 4: 1} == solution(words)
