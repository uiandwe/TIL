# -*- coding: utf-8 -*-
import asyncio

async def nested():
    return 42

async def test():
    # Nothing happens if we just call "nested()".
    # A coroutine object is created but not awaited,
    # so it *won't run at all*.
    nested()

    # Let's do it differently now and await it:
    print(await nested())  # will print "42".

if __name__ == '__main__':
    futures = [test()]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(futures))
    loop.close()
