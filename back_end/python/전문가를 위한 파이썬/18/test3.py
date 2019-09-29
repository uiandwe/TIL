# -*- coding: utf-8 -*-
import asyncio
import random

async def lazy_greet(msg, delay=1):
  print(msg, "will be displayed in", delay, "seconds")
  await asyncio.sleep(delay)
  return msg.upper()

async def main():
  messages = ['hello', 'world', 'apple', 'banana', 'cherry']
  fts = [asyncio.ensure_future(lazy_greet(m, random.randrange(1, 5)))
          for m in messages]
  (done, pending) = await asyncio.wait(fts, timeout=2)
  print(pending)
  if pending:
    print("there is {} tasks not completed".format(len(pending)))
    for f in pending:
      f.cancel()
  for f in done:
    x = await f
    print(x)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
