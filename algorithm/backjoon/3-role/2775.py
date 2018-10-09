
num1 = input()
num2 = input()

'''
1 5 ....
1 4 10 20 35 56 84 120 165 220 ...
1 3  6 10 15 21 28 36  45  55 ...
1 2  3  4  5  6  7  8   9  10..
'''

d = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]]
index = 1


for j in range(1, 14):
    temp = []
    for i in range(14):
        val = 1
        if i != 0:
            val = d[j-1][i] + temp[i-1]
        temp.append(val)
    d.append(temp)


print d[num1][num2-1]
