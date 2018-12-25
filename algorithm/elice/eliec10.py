import ast
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

# 입력 정보를 받아 location을 초기화 해 줍니다.
temp = ''
count = 0
while count < 7:
    temp += input() + ','
    count += 1

location = ast.literal_eval('{'+temp+'}')

region = []
for l in location:
    region.append(l)

map = [[0 for x in region] for y in region]
visite = [0 for x in region]
d = [[float('inf'), []] for x in region]
d[0][0] = 0
d[0][1] = ['Seoul']

for i in range(len(region)):
    temp_location = location[region[i]]
    for arrival in temp_location:
        map[i][region.index(arrival)] = temp_location[arrival]

q = queue()
q.push(0)

while q.empty() is False:
    temp_node = q.pop()
    visite[temp_node] = 1

    for i in range(len(map[temp_node])):
        path_weight = map[temp_node][i]
        if path_weight != 0:
            q.push(i)
            if d[i][0] > d[temp_node][0] + path_weight:
                d[i][0] = d[temp_node][0] + path_weight
                path_visite = ' '.join(d[temp_node][1])
                path_visite += ' '+region[i]
                d[i][1] = path_visite.split(" ")


print(d[-1][0])
for l in d[-1][1]:
    print(l)
