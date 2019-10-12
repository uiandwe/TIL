# -*- coding: utf-8 -*-
from concurrent.futures import wait, as_completed, ProcessPoolExecutor

def square(x):
    return x * x

executor = ProcessPoolExecutor(max_workers=4)

result = executor.map(square, [i for i in range(5)])

print(list(result))



###############################################################


fut1 = executor.submit(square, 2)
fut2 = executor.submit(square, 3)

wait([fut1, fut2])

result = as_completed([fut1, fut1])
print(list(result))


###########################################################

import random
import multiprocessing

samples = 1000000

def sample():

    x = random.uniform(-1.0, 1.0)
    y = random.uniform(-1.0, 1.0)

    if x ** 2 + y ** 2 <= 1:
        return 1
    else:
        return 0

# 병렬 계산에 많은 시간이 들어감(1000000을 돌림)
# pool = multiprocessing.Pool()
# results_async = [pool.apply_async(sample) for i in range(samples)]
# hits = sum(r.get() for r in results_async)
# print(hits)


# 개량형(10번 돌림)
def sample_multiple(samples_partial):
    return sum(sample() for i in range(int(samples_partial)))

n_tasks = 10
chunk_size = samples/n_tasks
pool = multiprocessing.Pool()
result_async = [pool.apply_async(sample_multiple, (chunk_size, )) for i in range(n_tasks)]
hits = sum(r.get() for r in result_async)
print(hits)



##########################################################33




