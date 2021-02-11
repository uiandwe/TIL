# -*- coding: utf-8 -*-
class Solution:
    def numberToWords(self, num: int) -> str:
        self.lessThan10 = ["", "일", "이", "삼", "사", "오", "육", "칠", "팔", "구", "십"]
        self.thousands = ["", "만", "억"]
        if num == 0:
            return "영"
        res = ''
        index = 0
        while num > 0:
            if num % 10000 != 0:
                res = self.helper(num % 10000) + self.thousands[index] + res
            num //= 10000
            index += 1

        replace_str = [("일십", "십"), ("일백", "백"), ("일천", "천"), ("일만", "만")]
        res = res.replace(" ", "")
        for r in replace_str:
            res = res.replace(r[0], r[1])

        return res

    def helper(self, num):
        if num == 0:
            return ""
        if num < 10:
            return self.lessThan10[num] + " "
        if num < 100:
            return self.lessThan10[num // 10] + "십" + self.helper(num % 10)
        if num < 1000:
            return self.lessThan10[num // 100] + "백" + self.helper(num % 100)
        if num < 10000:
            return self.lessThan10[num // 1000] + "천" + self.helper(num % 1000)


s = Solution()
assert s.numberToWords(1) == "일"
assert s.numberToWords(5) == "오"
assert s.numberToWords(8) == "팔"
assert s.numberToWords(9) == "구"
assert s.numberToWords(10) == "십"
assert s.numberToWords(15) == "십오"
assert s.numberToWords(20) == "이십"
assert s.numberToWords(55) == "오십오"
assert s.numberToWords(71) == "칠십일"
assert s.numberToWords(90) == "구십"
assert s.numberToWords(115) == "백십오"
assert s.numberToWords(100) == "백"
assert s.numberToWords(356) == "삼백오십육"
assert s.numberToWords(808) == "팔백팔"
assert s.numberToWords(1000) == "천"
assert s.numberToWords(1010) == "천십"
assert s.numberToWords(1111) == "천백십일"
assert s.numberToWords(4009) == "사천구"
assert s.numberToWords(7777) == "칠천칠백칠십칠"
assert s.numberToWords(10000) == "만"
assert s.numberToWords(34978) == "삼만사천구백칠십팔"
assert s.numberToWords(100000) == "십만"
assert s.numberToWords(999999) == "구십구만구천구백구십구"
assert s.numberToWords(1000000) == "백만"
assert s.numberToWords(10000000) == "천만"
assert s.numberToWords(100000000) == "일억"

