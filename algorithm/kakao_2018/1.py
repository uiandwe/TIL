# -*- coding: utf8 -*-

'''

https://www.welcomekakao.com/learn/courses/30/lessons/42888

record
["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]


result
["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]

'''

def solution(record):
    answer = []
    returnArray = []
    obj = {}

    for str in record:
        strArray = str.split(" ")

        if strArray[0] == 'Enter':
            obj[strArray[1]] = strArray[2]
            answer.append(['e', strArray[1]])
        elif strArray[0] == 'Leave':
            answer.append(['l', strArray[1]])
        else:
            obj[strArray[1]] = strArray[2]

    for index, text in enumerate(answer):
        text[1] = text[1].replace(text[1], obj[text[1]])
        if text[0] == 'e':
            text[1] += '님이 들어왔습니다.'
        else:
            text[1] += '님이 나갔습니다.'
        returnArray.append(text[1])
    return returnArray

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

print(solution(record))
