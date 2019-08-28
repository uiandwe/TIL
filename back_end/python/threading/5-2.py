# -*- coding: utf-8 -*-
# 해결방안 threading.Lock() # lock 생성

import logging
import concurrent.futures
import time
import threading

logging.getLogger().setLevel(logging.INFO)

class FakeDatabase:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock() # lock 생성

    def locked_update(self, name):
        logging.info("Thread %s: starting update", name)
        logging.debug("Thread %s about to lock", name)
        with self._lock: # with문 활용(acquire, release 자동 적용)
            logging.debug("Thread %s has lock", name)
            local_copy = self.value
            local_copy += 1
            time.sleep(0.1)
            self.value = local_copy
            logging.debug("Thread %s about to release lock", name)
        logging.debug("Thread %s after release", name)
        logging.info("Thread %s: finishing update", name)


database = FakeDatabase()
logging.info("Testing update. Starting value is %d.", database.value)
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    for index in range(2):
        executor.submit(database.locked_update, index)
logging.info("Testing update. Ending value is %d.", database.value)
