# 5! / 2! * (5-2)!

n = input()
k = input()

d = [0, 1]


for i in range(2, n+1):
    d.append(d[i-1] * i)

print d[n] / (d[k] * d[(n-k)])
