class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = str(x)
        if temp == temp[::-1]:
            return True
        return False
