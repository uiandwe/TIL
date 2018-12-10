
def solution(array, k):
    dict = {}
    for str in array:
        if str in dict:
            dict[str] += 1
        else:
            dict[str] = 1

    temp = sorted(dict, key=dict.get, reverse=True)[:k]
    print(temp)



solution(["i", "love", "leetcode", "i", "love", "coding"], 2)
solution(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4)
