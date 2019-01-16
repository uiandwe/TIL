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


def solution(node_count, nodes, start_node, end_node):
    d = [[0 for x in range(node_count+1)] for y in range(node_count+1)]
    visite_node = [0 for x in range(node_count+1)]
    weight_node = [float('inf') for x in range(node_count+1)]

    for node in nodes:
        s_node = node[0]
        e_node = node[1]
        weight = node[2]

        d[s_node][e_node] = weight

    q = queue()
    q.push(start_node)
    weight_node[start_node] = 0

    while q.empty() is False:
        now_node = q.pop()
        visite_node[now_node] = 1

        for i in range(len(d)):
            if d[now_node][i] > 0 and visite_node[i] == 0:

                if weight_node[i] > d[now_node][i] + weight_node[now_node]:
                    weight_node[i] = d[now_node][i] + weight_node[now_node]

                if visite_node[i] == 0:
                    q.push(i)

    return weight_node[end_node]
