# -*- coding: utf-8 -*-
import asyncio

async def test():
    print('hello')
    await asyncio.sleep(1)
    print('world')

if __name__ == '__main__':
    futures = [test()]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(futures))
    loop.close()

