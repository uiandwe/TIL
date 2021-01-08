# -*- coding: utf-8 -*-
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        preorder = preorder.split(",")
        if preorder[0] == '#' and len(preorder) > 1:
            return False

        count = 1
        for i in preorder:
            count -= 1
            if count < 0:
                return False
            if i != '#':
                count += 2

        return count == 0


s = Solution()
assert s.isValidSerialization("1,#,#") is True
assert s.isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#") is True
assert s.isValidSerialization("1,#") is False
assert s.isValidSerialization("9,#,#,1") is False
assert s.isValidSerialization("#,#,3,5,#") is False
assert s.isValidSerialization("#") is True
assert s.isValidSerialization("7,2,#,2,#,#,#,6,#") is False

