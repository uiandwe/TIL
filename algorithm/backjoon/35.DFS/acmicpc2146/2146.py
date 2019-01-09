class queue:
    array = []

    def push(self, num):
        self.array.append(num)

    def pop(self):
        if self.size() > 0:
            return self.array.pop(0)

    def size(self):
        return len(self.array)

    def empty(self):
        if len(self.array) > 0:
            return False
        else:
            return True


def island_dfs(x, y, map, num):

    map[x][y] = num

    position_x = [1, -1, 0, 0]
    position_y = [0, 0, 1, -1]
    n = len(map)

    for i in range(4):
        next_x = x + position_x[i]
        next_y = y + position_y[i]

        if 0 <= next_x and n > next_x and 0 <= next_y and n > next_y:
            if map[next_x][next_y] == 1:
                island_dfs(next_x, next_y, map, num)


def short_island(x, y, map, path_map, island_now_num):

    position_x = [1, -1, 0, 0]
    position_y = [0, 0, 1, -1]
    n = len(map)

    min_val = float('inf')
    check_other_island = False
    for i in range(4):
        next_x = x + position_x[i]
        next_y = y + position_y[i]

        if 0 <= next_x and n > next_x and 0 <= next_y and n > next_y:
            if path_map[next_x][next_y] > 0:
                min_val = min(min_val, path_map[next_x][next_y])
            if map[next_x][next_y] > 0 and map[next_x][next_y] != island_now_num:
                check_other_island = True

    if path_map[x][y] == min_val + 1:
        return float('inf')

    path_map[x][y] = min_val + 1

    if map[x][y] == island_now_num:
        path_map[x][y] = 1

    if check_other_island is True and map[x][y] == 0:
        return path_map[x][y]

    for i in range(4):
        next_x = x + position_x[i]
        next_y = y + position_y[i]

        if 0 <= next_x and n > next_x and 0 <= next_y and n > next_y:
            if map[next_x][next_y] == 0:
                return short_island(next_x, next_y, map, path_map, island_now_num)

    return float('inf')


def solution(map):
    n = len(map)
    q = queue()

    ## 섬찾기
    island_num = 1
    for i in range(n):
        for j in range(n):
            if map[i][j] == 1:
                island_num += 1
                q.push(island_num)
                island_dfs(i, j, map, island_num)


    ## 최단길이 찾기
    min_length = float('inf')

    while q.empty() is False:
        island_now_num = q.pop()
        path_map = [[0 for x in range(n)] for y in range(n)]
        for i in range(n):
            for j in range(n):
                if map[i][j] == island_now_num:
                    min_length = min(min_length, short_island(i, j, map, path_map, island_now_num))

    return min_length-1

