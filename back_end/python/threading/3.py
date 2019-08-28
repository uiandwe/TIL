# -*- coding: utf-8 -*-

import logging
import threading
import time

logging.getLogger().setLevel(logging.INFO)


def thread_function(name):
    logging.info(f'Thread {name}: starting')
    time.sleep(2)
    logging.info(f'Thread {name}: finishing')


threads = list()
for index in range(3):
    logging.info("Main    : create and start thread %d.", index)
    x = threading.Thread(target=thread_function, args=(index,))
    threads.append(x)
    x.start()

for index, thread in enumerate(threads):
    thread.join() # 각각의 thread가 끝나기를 기다린다.
    logging.info("Main    : thread %d done", index)
