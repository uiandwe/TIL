class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        d = [0, 0]
        for point in moves:
            if point == "R":
                d[0] += 1
            elif point == "L":
                d[0] -= 1
            elif point == "U":
                d[1] += 1
            elif point == "D":
                d[1] -= 1

        if d[0] == 0 and d[1] == 0:
            return True
        else:
            return False 
