# -*- coding: utf-8 -*-
import asyncio

class AsyncIterator:
    def __init__(self, obj):
        self.obj = obj

    async def __aiter__(self):
        return self

    async def __anext__(self):
        try:
            return next(self.obj)
        except StopIteration:  # 이터레이션이 끝일 경우
            raise StopAsyncIteration


async def example():
    _map = map(lambda x: x * 2, [1, 2, 3])
    _iter = AsyncIterator(_map)
    async for x in _iter:
        print(x, end= ' ')

loop = asyncio.get_event_loop()
loop.run_until_complete(example())
