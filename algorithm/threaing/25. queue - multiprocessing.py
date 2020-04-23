# -*- coding: utf-8 -*-
from multiprocessing import Pool
import multiprocessing
import queue
import time

def myTask(queue):
  value = queue.get()
  print("Process {} Popped {} from the shared Queue".format(multiprocessing.current_process().pid, value))
  queue.task_done()

def main():
  m = multiprocessing.Manager()
  sharedQueue = m.Queue()
  for i in range(3):
    sharedQueue.put(i)

  for i in range(3):
    process1 = multiprocessing.Process(target=myTask, args=(sharedQueue,))
    process1.start()
    process1.join()


if __name__ == '__main__':
  main()
