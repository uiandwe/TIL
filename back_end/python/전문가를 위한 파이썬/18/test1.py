# -*- coding: utf-8 -*-

import asyncio
import time

async def lazy_greet(msg, delay=1):
  await asyncio.sleep(delay)
  print(msg)

loop = asyncio.get_event_loop()
loop.run_until_complete(lazy_greet("hello", 3))


async def main():
    print('hello')
    await asyncio.sleep(1)
    print('world')


result = loop.run_until_complete(main())


async def say_after(delay, what):
    # await asyncio.sleep(delay)
    print(what)

async def main1():
    print(f"started at {time.strftime('%X')}")

    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")


result1 = loop.run_until_complete(main1())
loop.close()
