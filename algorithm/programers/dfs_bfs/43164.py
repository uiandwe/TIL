# -*- coding: utf-8 -*-
import copy
answer = []


def dfs(start, tickets, visite, trip):

    if sum(visite) == len(tickets):
        answer.append(copy.deepcopy(trip))

    for index, node in enumerate(tickets):
        if start[1] == node[0] and visite[index] == 0:
            visite[index] = 1
            trip.append(node)

            dfs(node, tickets, visite, trip)
            visite[index] = 0
            trip.pop(len(trip)-1)

    return


def answer_str(array):
    temp = array.pop(0)
    for t1 in array:
        temp.append(t1[1])

    return temp


def solution(tickets):
    global answer
    answer = []

    for index, start in enumerate(tickets):
        if start[0] == "ICN":
            visite = [0 for x in tickets]
            visite[index] = 1
            dfs(start, tickets, visite, [start])

    min_path = answer_str(answer.pop(0))

    for i in answer:
        temp = answer_str(i)
        if ''.join(min_path) > ''.join(temp):
            min_path = copy.deepcopy(temp)

    # print(min_path)

    return min_path



print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
