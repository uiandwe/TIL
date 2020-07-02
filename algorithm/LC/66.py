class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        temp = [str(i) for i in digits]
        temp = str(int(''.join(temp))+1)
        temp.split()
        return temp
