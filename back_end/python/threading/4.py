# -*- coding: utf-8 -*-
import concurrent.futures
import logging
import time

logging.getLogger().setLevel(logging.INFO)

def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor: # with와 함께 사용을 권장
    executor.map(thread_function, [0,1,2]) # list와 같은 형태로 args를 전달하면 thread에 하나씩 전달된다. (한 번에 실행)
    # executor.submit(thread_function, 0) # thread마다 args를 각각 전달하는 코드 (반복 실행)
    # executor.submit(thread_function, 1)
    # executor.submit(thread_function, 2)
