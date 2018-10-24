a = []
d = []

for i in range(11):
    str = raw_input()
    str = str.split(" ")
    startTime = int(str[0])
    endTime = int(str[1])

    a.append([startTime, endTime])

print a


a.sort(key=lambda x:x[1])

print a

d.append(a[0])

for i in a:
    temp = d[len(d)-1]
    
    if temp[1] <= i[0] and temp[0] != i[0] and temp[1] != i[1]:
        d.append(i)
        
print d
