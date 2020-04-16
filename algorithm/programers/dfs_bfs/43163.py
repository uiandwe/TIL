# -*- coding: utf-8 -*-
result_answer = float('inf')

def is_word_right(word1, word2):
    count = 0
    for w1, w2 in zip(word1, word2):
        if w1 == w2:
            count += 1

    if count == len(word1) - 1:
        return True
    return False


def dfs(word, words, target, answer, visite):
    global result_answer

    if word == target:
        return answer

    for index, pw in enumerate(words):
        if is_word_right(word, pw) and visite[index] == 0:
            visite[index] = 1
            temp_answer = dfs(pw, words, target, answer+1, visite)
            if result_answer > temp_answer:
                result_answer = temp_answer
            visite[index] = 0

    return float('inf')

def solution(begin, target, words):

    words = [word for word in words if len(word) == len(target)]
    if target not in words:
        return 0

    visite = [0 for x in words]

    dfs(begin, words, target, 0, visite)
    return result_answer


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))

