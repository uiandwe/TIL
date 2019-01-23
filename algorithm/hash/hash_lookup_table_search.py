def solution(arr, searchWord):
    dict = {}
    for index, word in enumerate(arr):
        hash_key = get_key(word.lower())
        if hash_key in dict:
            dict[hash_key].append(index)
        else:
            dict[hash_key] = [index]

    word_key = get_key(searchWord)
    for index in dict[word_key]:
        if arr[index] == searchWord:
            return index

    return -1


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
             "lovable",
             "moonlight"
             ]
    assert 9 == solution(words, "moonlight")
