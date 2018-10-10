def merge(leftList, rightList):
    result = []
    while len(leftList) > 0 and len(rightList):
        if leftList[0] <= rightList[0]:
            result.append(leftList.pop(0))
        else:
            result.append(rightList.pop(0))
    while len(leftList) > 0:
        result.append(leftList.pop(0))
    while len(rightList) > 0:
        result.append(rightList.pop(0))

    return result


def merge_sort(list):
    if len(list) <= 1:
        return list

    mid = len(list) // 2
    leftList = list[:mid]
    rightList = list[mid:]
    leftList = merge_sort(leftList)
    rightList = merge_sort(rightList)

    return merge(leftList, rightList)


a = [9,8,7,6,5,4,3,2,1,10]

print merge_sort(a)
