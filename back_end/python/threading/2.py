# -*- coding: utf-8 -*-
import logging
import threading
import time

logging.getLogger().setLevel(logging.INFO)


def thread_function(name):
    logging.info(f'Thread {name}: starting')
    time.sleep(2)
    logging.info(f'Thread {name}: finishing')


logging.info("Main    : before creating thread")
x = threading.Thread(target=thread_function, args=(1,))
logging.info("Main    : before running thread")
x.start()
logging.info("Main    : wait for the thread to finish")
logging.info("Main    : all done. Waiting non-daemon threads to finish")
