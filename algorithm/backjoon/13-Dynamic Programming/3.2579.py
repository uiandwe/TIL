

d = []

array = [0, 10, 20, 15, 25, 10, 20]

num = len(array)

for i in range(len(array)):
    d.append(0)

for i in range(1, 3):
    if i == 1:
        d[i] = max(d[i-1] + array[i], array[i])
    else:
        d[i] = max(d[i-2] + array[i], array[i-1] + array[i])


for i in range(3, num):
    d1 = d[i-3]+array[i-1]+array[i]
    d2 = d[i-2]+array[i]
    d[i] = max(d1, d2)

print d
