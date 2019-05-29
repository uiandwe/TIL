# # -*- coding: utf-8 -*-
import asyncio
import random

async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")
    return random.randint(0, 10)

async def main():
    res = await asyncio.gather(*(count() for i in range(3)))
    return res

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    loop = asyncio.get_event_loop()
    r1 = loop.run_until_complete(main())
    print(r1)

    loop.close()
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")








import time

def count():
    print("One")
    time.sleep(1)
    print("Two")

def main():
    for _ in range(3):
        count()

if __name__ == "__main__":
    s = time.perf_counter()
    main()
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
