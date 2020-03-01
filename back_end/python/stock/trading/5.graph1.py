# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

fig = plt.figure()

# 가로
ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)



# ax1 = fig.add_subplot(1, 2, 1)
# ax2 = fig.add_subplot(1, 2, 2)

# 세로
# plt.show()


x = range(0, 100)
y = [v*v for v in x]
ax1.plot(x, y)
ax2.bar(x, y)
plt.show()
