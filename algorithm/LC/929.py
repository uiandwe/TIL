# -*- coding: utf-8 -*-
from typing import *
from collections import defaultdict
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        s = set()

        for e in emails:
            # @로 나누기
            adr, domain = e.split("@")
            # + 앞으로 자르기
            adr = adr.split("+")[0]
            # . 지우기
            adr = adr.replace(".", "")
            # d에 넣기
            s.add(adr+"@"+domain)

        return len(s)


s = Solution()
assert s.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]) == 2
assert s.numUniqueEmails(["testemail@leetcode.com","testemail1@leetcode.com","testemail+david@lee.tcode.com"]) == 3
