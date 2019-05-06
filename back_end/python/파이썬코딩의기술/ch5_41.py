# -*- coding: utf-8 -*-
def gcd(pair):
    a, b = pair
    low = min(a, b)
    for i in range(low, 0, -1):
        if a % i == 0 and b % i == 0:
            return i


numbers = [(12347123, 323424324), (234987123, 723908213), (345123123, 67584123)]
from time import time
start = time()
result = list(map(gcd, numbers))
end = time()

print(end - start)

# GIL 로 똑같은 서능
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
start = time()
pool = ThreadPoolExecutor(max_workers=2)
results = list(pool.map(gcd, numbers))
end = time()
print(end-start)

# CPU 별로 나눠서 작업 / 빨라짐
start = time()
pool = ProcessPoolExecutor(max_workers=2)
results = list(pool.map(gcd, numbers))
print(results)
end = time()
print(end - start)
