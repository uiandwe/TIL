# -*- coding: utf-8 -*-
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
import random


def checkStatus(i, j):
    print(i, j)
    time.sleep(i)
    return random.randint(1, 10)


def printStatus(statusCode):
    print("URL Crawled with status code: {}".format(statusCode))


def main():

    with ThreadPoolExecutor(max_workers=3) as executor:

        tasks = []
        for i in range(10):
            task = executor.submit(checkStatus, i, i)
            tasks.append(task)

        for future in as_completed(tasks):
            print(future.result())


if __name__ == '__main__':
    main()
