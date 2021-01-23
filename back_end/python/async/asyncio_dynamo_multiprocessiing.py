# -*- coding: utf-8 -*-

import asyncio
from multiprocessing import Process, current_process, Manager, pool
import os
import aioboto3
import queue


async def fetch(d):
    async with aioboto3.resource('dynamodb', region_name='ap-northeast-2') as dynamo_resource:
        table = await dynamo_resource.Table('test.ws-record')
        for data in d:
            await table.put_item(Item={'key': 'test'+str(data), 'ref_dt': '20210123', 'option': data})


def myTask(q, arg):
    print("arg", arg)
    while True:
        try:
            value = q.get_nowait()
            print("Process {} Popped {} from the shared Queue {}".format(current_process().pid, value, arg))
            d = [i for i in range(arg*5, arg*5+5)]
            loop = asyncio.get_event_loop()
            loop.run_until_complete(fetch(d))
        except queue.Empty:
            break
    print("done : ", arg)

def main():
    m = Manager()
    sharedQueue = m.Queue()
    processes = []

    for i in range(20):
        sharedQueue.put(i)

    for w in range(os.cpu_count()):
        p = Process(target=myTask, args=(sharedQueue, w))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()


if __name__ == '__main__':
    main()
