import asyncio


async def buzzer1():
    for i in range(10):
        print("beep 1")
        await asyncio.sleep(2)

async def buzzer2():
    for i in range(10):
        print("beep 2")
        await asyncio.sleep(3)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait([buzzer1(), buzzer2()]))
