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


def dijkstra(len_node, d, start_node, end_node):

    visite_node = [0 for x in range(len_node + 1)]
    weight_node = [float('inf') for x in range(len_node + 1)]


    q = queue()
    q.push(start_node)
    weight_node[start_node] = 0

    while q.empty() is False:
        now_node = q.pop()
        visite_node[now_node] = 1
        for i in range(1, len_node+1):
            if d[now_node][i] > 0:

                if weight_node[i] > d[now_node][i] + weight_node[now_node]:
                    weight_node[i] = d[now_node][i] + weight_node[now_node]

                if visite_node[i] == 0:
                    q.push(i)

    if start_node == end_node:
        return weight_node
    else:
        return weight_node[end_node]


def solution(len_node, nodes, end_node):

    d = [[0 for x in range(len_node + 1)] for y in range(len_node + 1)]

    for i in nodes:
        s_node = i[0]
        e_node = i[1]
        weight = i[2]
        d[s_node][e_node] = weight

    visite_weight = [0 for x in range(len_node+1)]
    for i in range(1, len_node+1):
        if i != end_node:
            visite_weight[i] = dijkstra(len_node, d, i, end_node)

    reverse_visite_weight = dijkstra(len_node, d, end_node, end_node)

    total_visite_weight = []
    for i in range(1, len_node+1):
        total_visite_weight.append(visite_weight[i] + reverse_visite_weight[i])

    return max(total_visite_weight)

