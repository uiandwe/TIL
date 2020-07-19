# -*- coding: utf-8 -*-
tmp_arr = [i for i in range(1, 9)]

k = 5 - 1

cut_point = len(tmp_arr)-k

print(tmp_arr[cut_point:]+tmp_arr[0:cut_point])
