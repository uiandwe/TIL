def q(array):
    if len(array) <= 1:
        return array

    pivot = array[len(array)//2]
    less = []
    qu = []
    more = []

    for val in array:
        if val == pivot:
            qu.append(val)
        elif val > pivot:
            more.append(val)
        else:
            less.append(val)

    return q(less)+qu+q(more)


a = [4, 6, 7, 8, 10, 3, 1, 14, 56, 31, 2]

print q(a)

