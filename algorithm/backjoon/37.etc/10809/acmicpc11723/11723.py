def solution(arr):
    d = [0 for x in range(21)]
    ret_arr = []
    for op in arr:
        if op[0] == "add":
            d[op[1]] = 1
        elif op[0] == "check":
            ret_arr.append(d[op[1]])
        elif op[0] == "remove":
            d[op[1]] = 0
        elif op[0] == "toggle":
            d[op[1]] ^= 1
        elif op[0] == "all":
            for i in range(len(d)):
                d[i] = 1
        elif op[0] == "empty":
            for i in range(len(d)):
                d[i] = 0

    return ret_arr


