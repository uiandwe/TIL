class queue:
    def __init__(self):
        self.array = []

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


def dijkstra(node_num, map):

    q = queue()
    q.push(node_num)

    n = len(map)
    visite_node = [0 for x in range(n)]
    d = [0 for x in range(n)]
    visite_node[node_num] = 1

    while q.empty() is False:
        temp_node = q.pop()
        for i in range(1, n):
            if map[temp_node][i] > 0 and visite_node[i] == 0:
                visite_node[i] = 1
                q.push(i)
                d[i] = d[temp_node] + map[temp_node][i]

    return max(d)


def solution(n, array):
    map = [[0 for x in range(n+1)] for y in range(n+1)]

    for node in array:
        node1 = node[0]
        node2 = node[1]
        weight = node[2]

        map[node1][node2] = weight
        map[node2][node1] = weight

    end_point_node = []
    for i in range(len(map)):
        if len([1 for i in map[i] if i > 0]) == 1:
            end_point_node.append(i)

    max_path_length = 0
    for node_num in end_point_node:
        temp_length = dijkstra(node_num, map)
        max_path_length = max(max_path_length, temp_length)

    return max_path_length
