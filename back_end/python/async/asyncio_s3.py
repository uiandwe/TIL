# -*- coding: utf-8 -*-

import asyncio
import aioboto3



async def fetch(i):
    async with aioboto3.resource("s3") as s3:
        bucket = await s3.Bucket('haezoom-config')
        async for s3_object in bucket.objects.all():
            print(i, s3_object)

async def main():
    futures = [asyncio.ensure_future(fetch(i)) for i in range(2)]
    result = await asyncio.gather(*futures)
    print(result)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()

