# -*- coding: utf-8 -*-
from collections import deque


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q = deque()
        for key in rooms[0]:
            q.append(key)
        visite = [0 for i in range(len(rooms))]
        visite[0] = 1

        while q:
            room = q.popleft()
            if visite[room]:
                continue

            visite[room] = 1
            for key in rooms[room]:
                if not visite[key]:
                    q.append(key)

        if sum(visite) == len(rooms):
            return True
        else:
            return False




