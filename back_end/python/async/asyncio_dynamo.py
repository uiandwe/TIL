# -*- coding: utf-8 -*-

import asyncio
import aioboto3

d = [i for i in range(2)]

async def fetch(d):
    async with aioboto3.resource('dynamodb', region_name='ap-northeast-2') as dynamo_resource:
        table = await dynamo_resource.Table('test.ws-record')
        for data in d:
            await table.put_item(Item={'key': 'test'+str(data), 'ref_dt': '20210123', 'option': data})

loop = asyncio.get_event_loop()
loop.run_until_complete(fetch(d))
