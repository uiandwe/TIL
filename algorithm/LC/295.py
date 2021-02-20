# -*- coding: utf-8 -*-
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.d = []

    def addNum(self, num: int) -> None:
        self.d.append(num)
        self.d.sort()

    def findMedian(self) -> float:
        m = len(self.d) // 2
        if len(self.d) % 2 == 0:
            # print(m, self.d[m])
            return (self.d[m-1] + self.d[m]) / 2
        else:
            return self.d[m]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


m = MedianFinder()
m.addNum(1)
m.addNum(2)
print(m.findMedian())
m.addNum(3)
print(m.findMedian())
m.addNum(4)
print(m.findMedian())
