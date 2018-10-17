# -*- coding: utf8 -*-

'''
한줄씩 같은 색상으로 칠할수 없음 == 한줄씩 띄어서 색상을 하나만 칠하면 됨
페인트의 가장 최소 비용 == 한줄에서 가장 작은 값
전체를 칠하는데 최솟값 == 한줄씩 칠하면서 최소값만을 더한값 (같은 색상은 연속할수 없다)
예제에서는 0, 2, 0 번째를 칠해서 26+57+13 = 96이 나옴 (연속할수 없기에 26+49+13은 정답이 되질 않음)
'''

rgb = [
    [0, 0, 0],
    [26, 40, 83],
    [49, 60, 57],
    [13, 89, 99]
]

result = 0

for i in range(1, len(rgb)):
    rgb[i][0] = min(rgb[i-1][1], rgb[i-1][2]) + rgb[i][0]
    rgb[i][1] = min(rgb[i-1][0], rgb[i-1][2]) + rgb[i][1]
    rgb[i][2] = min(rgb[i-1][0], rgb[i-1][1]) + rgb[i][2]

print min(rgb[len(rgb)-1][0],rgb[len(rgb)-1][1],rgb[len(rgb)-1][2])