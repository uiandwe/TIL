# -*- coding: utf-8 -*-
"""

1.
First, go through an example.

This buys time, makes sure you understand the problem,

and lets you gain some intuition for the problem.

For example,

if we had [[10, 15, 30], [12, 15, 20], [17, 20, 32]],

the result should be [10, 12, 15, 15, 17, 20, 20, 30, 32].

2.
Next, give any solution you can think of (even if it's brute force).

It seems obvious that if we just flattened the lists and sorted it,

we would get the answer we want.

The time complexity for that would be O(KN log KN),

since we have K * N total elements.

"""

import heapq

def solution(lists):
    merged_list = []

    heap = [(lst[0], i, 0) for i, lst in enumerate(lists) if lst]
    heapq.heapify(heap)

    while heap:
        val, list_ind, element_ind = heapq.heappop(heap)

        merged_list.append(val)

        if element_ind + 1 < len(lists[list_ind]):
            next_tuple = (lists[list_ind][element_ind + 1],
                          list_ind,
                          element_ind + 1)
            heapq.heappush(heap, next_tuple)
    return merged_list


print(solution([[10, 15, 30], [12, 15, 20], [17, 20, 32]]))
