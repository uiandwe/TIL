class Solution:
    d = [0,1]

    def fibo(self, n):

        if n == 0:
            return self.d[0]
        elif n == 1:
            return self.d[1]

        if len(self.d) == n+1:
            return self.d[n]

        dLen = len(self.d)
        a = self.d[dLen-1] + self.d[dLen-2]
        self.d.append(a)
        return self.fibo(n)

    def solution(self, n):
        return self.fibo(n)
