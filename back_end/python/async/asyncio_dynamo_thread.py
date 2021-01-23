# -*- coding: utf-8 -*-

import asyncio
import aioboto3



async def fetch(d):
    async with aioboto3.resource('dynamodb', region_name='ap-northeast-2') as dynamo_resource:
        table = await dynamo_resource.Table('test.ws-record')
        for data in d:
            await table.put_item(Item={'key': 'test'+str(data), 'ref_dt': '20210123', 'option': data})

from multiprocessing import Process
import time

def buzzer1():
    d = [i for i in range(5)]

    loop = asyncio.get_event_loop()
    loop.run_until_complete(fetch(d))

def buzzer2():
    d = [i for i in range(6, 10)]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(fetch(d))

if __name__ == '__main__':
    p1 = Process(target=buzzer1)
    p2 = Process(target=buzzer2)
    p1.start()
    p2.start()
