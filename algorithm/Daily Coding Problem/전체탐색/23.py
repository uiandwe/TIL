# -*- coding: utf-8 -*-
"""
https://www.hackerrank.com/challenges/maxsubarray/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

We define subsequence as any subset of an array. We define a subarray as a contiguous subsequence in an array.

Given an array, find the maximum possible sum among:

    all nonempty subarrays.
    all nonempty subsequences.

Print the two values as space-separated integers on one line.

Note that empty subarrays/subsequences should not be considered.

For example, given an array
, the maximum subarray sum is comprised of element inidices and the sum is . The maximum subsequence sum is comprised of element indices and the sum is

.

Function Description

Complete the maxSubarray function in the editor below. It should return an array of two integers: the maximum subarray sum and the maximum subsequence sum of

.

maxSubarray has the following parameter(s):

    arr: an array of integers

Input Format

The first line of input contains a single integer

, the number of test cases.

The first line of each test case contains a single integer
.
The second line contains space-separated integers where

.

Constraints

The subarray and subsequences you consider should have at least one element.

Output Format

Print two space-separated integers denoting the maximum sums of nonempty subarrays and nonempty subsequences, respectively.

Sample Input 0

2
4
1 2 3 4
6
2 -1 2 3 4 -5

Sample Output 0

10 10
10 11

Explanation 0

In the first case: The maximum sum for both types of subsequences is just the sum of all the elements since they are all positive.

In the second case: The subarray
is the subarray with the maximum sum, and

is the subsequence with the maximum sum.

Sample Input 1

1
5
-2 -3 -1 -4 -6

Sample Output 1

-1 -1

"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubarray function below.
def maxSubarray(arr):
    d = [[0 for _ in arr] for i in range(2)]

    max_answer2 = max_answer1 = d[1][0] = d[0][0] = arr[0]

    for i in range(1, len(arr)):
        d[0][i] = max(arr[i]+d[0][i-1], arr[i])
        max_answer1 = max(max_answer1, d[0][i])

        temp1 = d[1][i-1]
        if d[1][i-1] <= 0:
            temp1 = 0
        temp2 = arr[i]
        if arr[i] <= 0:
            temp2 = 0
        d[1][i] = max(temp2 + temp1, temp2)
        max_answer2 = max(max_answer2, d[1][i])

    if max_answer1 <= 0:
        max_answer2 = max_answer1

    # print(d[0], max_answer1)
    # print(d[1], max_answer2)

    print(max_answer1, max_answer2)

maxSubarray([-1, 2, 3, -4, 5, 10])
maxSubarray([1, 2, 3, 4])
maxSubarray([2, -1, 2, 3, 4, -5])
maxSubarray([-2, -3, -1, -4, -6])
maxSubarray([0])
