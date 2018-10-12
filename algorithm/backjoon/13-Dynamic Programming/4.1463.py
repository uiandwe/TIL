d = []


# def go(n):
#     if n == 1:
#         return 0
#     if d[n] > 0:
#         return d[n]
#     d[n] = go(n-1)+1
#
#     if n%2 == 0:
#         temp = go(n/2)+1
#         if d[n] > temp:
#             d[n] = temp
#     if n%3 == 0:
#         temp = go(n/3)+1
#         if d[n] > temp:
#             d[n] = temp
#
#     return d[n]
#
#
num = input()
#
# for i in range(num+1):
#     d.append(0)
#
# print go(num)
# print d


d = [0, 0]

for i in range(2, num+1):
    d.append(d[i-1]+1)

    if i%2 == 0 and d[i] > d[i/2] +1:
        d[i] = d[i/2] +1
    if i%3 == 0 and d[i] > d[i/3] + 1:
        d[i] = d[i/3] + 1



print d
