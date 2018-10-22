def q(a):
    if len(a) <= 1:
        return a

    pivot = a[len(a) // 2]
    less = []
    equal = []
    more = []

    for i in a:
        if i > pivot:
            more.append(i)
        elif i < pivot:
            less.append(i)
        else:
            equal.append(i)

    return q(less)+ equal + q(more)



a = [5, 4, 6, 100, 9, 8, 1, 24, 63, 12]

print q(a)
