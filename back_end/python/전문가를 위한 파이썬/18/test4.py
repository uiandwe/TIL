# -*- coding: utf-8 -*-


import asyncio
import random

async def lazy_greet(msg, delay=1):
  print(msg, "will be displayed in", delay, "seconds")
  await asyncio.sleep(delay)
  return msg.upper()

async def time_log():
  i = 0
  print("time log starts.")
  while True:
    await asyncio.sleep(1)
    i += 1
    print('...%02d sec.' % (i,))

async def main():
  t = asyncio.ensure_future(time_log())
  messages = ['hello', 'world', 'apple', 'banana', 'cherry']
  fts = [asyncio.ensure_future(lazy_greet(m, random.randrange(1, 5)))
    for m in messages]
  result = await asyncio.gather(*fts)
  t.cancel()
  print(result)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
