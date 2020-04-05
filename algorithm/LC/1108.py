# -*- coding: utf-8 -*-
import re

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return re.sub('[\.]+', "[.]", address)

s = Solution()
s.defangIPaddr("1.1.1.1")
