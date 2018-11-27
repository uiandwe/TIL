def comparePoint(a, b):
    if a[0] <= b[0] and a[1] >= b[1]:
        return False
    else:
        return True

def solution(line, array):
    a = []
    for point in array:
        if point[0] > point[1]:
            a.append([point[0], point[0]+(line-point[0])+point[1], 0])
        else:
            a.append([point[0], point[1], 0])

    a = sorted(a, key=lambda x:x[0])

    b = [a[0]]
    for i in range(1, len(a)):
        if comparePoint(a[i-1], a[i]):
            b.append(a[i])

    for point in b:
        if point[1] <= line:
            point[0] += line
            point[1] += line


    b = sorted(b, key=lambda x:x[0], reverse=True)


    d = []
    for i in range(1, len(b)):
        if b[i-1][0] >= b[i][0] and b[i-1][1] <= b[i][1]:
            pass
        else:
            d.append(b[i-1])
    d.append(b[-1])
    
    print(d)


solution(10, [[0, 4], [2, 6], [5, 0], [7, 9], [9, 4]])
