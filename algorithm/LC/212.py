class queue:
    def __init__(self):
        self.array = []

    def push(self, data):
        self.array.append(data)

    def pop(self):
        if self.empty() is False:
            return self.array.pop(0)
        else:
            return -1

    def empty(self):
        if self.size() > 0:
            return False
        else:
            return True

    def size(self):
        return len(self.array)



map = [
    ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]


position_x = [1, -1, 0, 0]
position_y = [0, 0, 1, -1]

returnArray = []

def dfs(position, str, visite, pick):
    x = position[0]
    y = position[1]

    if map[x][y] == str[pick]:
        visite[pick] = 1
        pick += 1

        if sum(visite) == len(str):
            returnArray.append(str)
            return

        for i in range(4):
            next_x = x+position_x[i]
            next_y = y+position_y[i]

            if next_x >= 0 and next_x <= len(map)-1 and next_y >= 0 and next_y <= len(map)-1:
                dfs([next_x, next_y], str, visite, pick)




def solution(array):
    print(array)
    for str in array:
        q = queue()
        for i in range(len(map)):
            for j in range(len(map[0])):
                if map[i][j] == str[0]:
                    q.push([i, j])

        while q.empty() is False:
            visite = [0 for x in str]
            dfs(q.pop(), str, visite, 0)

    print(returnArray)

solution(["oath","pea","eat","rain"])
