def solution(weight, backpack):
    d = [0 for x in range(weight+1)]

    for i in range(len(backpack)):
        temp_weight = backpack[i][0]
        temp_value = backpack[i][1]
        for j in range(weight+1):
            if j-temp_weight >= 0:
                d[j] = max(d[j], d[j-temp_weight] + temp_value)

    return d[weight]

