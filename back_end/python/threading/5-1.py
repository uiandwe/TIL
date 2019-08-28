# -*- coding: utf-8 -*-
"""
Race condition
두 개 이상의 thread가 공유 자원을 사용할 때 잘못된 결과가 발생할 수 있는 상황을 말한다.
3이 나와야 하지만 1이 나옴
즉 1+1+1 이 되어야 할 상황에서 0으로 계속 초기화 하였고, 마지막+1 만 동작하여, 1이 출력
"""
import logging
import concurrent.futures
import time

logging.getLogger().setLevel(logging.INFO)

class FakeDatabase:
    def __init__(self):
        self.value = 0

    def update(self, name):
        logging.info("Thread %s: starting update", name)
        local_copy = self.value
        local_copy += 1
        time.sleep(0.1)
        self.value = local_copy
        logging.info("Thread %s: finishing update", name)




database = FakeDatabase()
logging.info("Testing update. Starting value is %d.", database.value)

with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    for index in range(1,4):
        executor.submit(database.update, index)

logging.info("Testing update. Ending value is %d.", database.value)
