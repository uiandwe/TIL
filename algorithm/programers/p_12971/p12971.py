def solution(sticker):
    if len(sticker) == 1:
        return sticker[0]

    d = [[0, 0] for i in range(len(sticker))]

    d[0][1] = sticker[0]
    d.insert(0, [0, 0])
    d.insert(0, [0, 0])
    sticker.insert(0, 0)
    sticker.insert(0, 0)

    for i in range(3, len(sticker)):
        d[i][0] = max(d[i-3][0], d[i-2][0]) + sticker[i]
        d[i][1] = max(d[i-3][1], d[i-2][1]) + sticker[i]

    d[len(d)-1][1] -= sticker[len(sticker)-1]

    return max(max(d))
