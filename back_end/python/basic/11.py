# -*- coding: utf-8 -*-
# heapq
# 최소힙 (작은거부터 )
import heapq

heap = []

heapq.heappush(heap, 4)
heapq.heappush(heap, 1)
heapq.heappush(heap, 7)
heapq.heappush(heap, 3)
print(heap)

pop = heapq.heappop(heap)
print(pop)
print(heap)


print(heapq.heappop(heap))
print(heap)


print(heap[0])


heap = [4, 1, 7, 3, 8, 5]
heapq.heapify(heap)
print(heap)


# 최대 힙 (큰거 부터)

nums = [4, 1, 7, 3, 8, 5]
heap = []

for num in nums:
  heapq.heappush(heap, (-num, num))  # (우선 순위, 값)

while heap:
  print(heapq.heappop(heap)[1])  # index 1


# k번째 최소값/최대값

def kth_smallest(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)

    kth_min = None
    for _ in range(k):
        kth_min = heapq.heappop(heap)

    return kth_min

print(kth_smallest([4, 1, 7, 3, 8, 5], 3))


# 힙정렬

def heap_sort(nums):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)

    sorted_nums = []
    while heap:
        sorted_nums.append(heapq.heappop(heap))
    return sorted_nums


print(heap_sort([4, 1, 7, 3, 8, 5]))


