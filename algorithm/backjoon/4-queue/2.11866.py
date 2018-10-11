import queue

q = queue.Queue()

num1 = input()
num2 = input()
result = []
for i in range(1, num1+1):
    q.push(i)

index = 0
while q.empty() is False :
    index += 1
    temp = q.pop()
    if index == num2:
        result.append(temp)
        index = 0
    else:
        q.push(temp)

print result

