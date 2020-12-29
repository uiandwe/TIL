# -*- coding: utf-8 -*-
class Solution:
    def readBinaryWatch(self, num: int):
        hour = 0
        minute = 0
        ret = set()
        for i in range(60*24):

            if "{0:b}".format(hour).count('1') + "{0:b}".format(minute).count('1') == num:
                ret.add("{}:{}".format(hour, str(minute).zfill(2)))

            if minute >= 59:
                minute = 0
                hour += 1
                if hour >= 12:
                    hour = 0
            else:
                minute += 1
        print(ret)
        return ret

s = Solution()
aa = s.readBinaryWatch(1)
for a in aa:
    if a not in ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]:
        assert False, a
# assert s.readBinaryWatch(0) == ["0:00"]
aa = s.readBinaryWatch(2)
for a in aa:
    if a not in ["0:03","0:05","0:06","0:09","0:10","0:12","0:17","0:18","0:20","0:24","0:33","0:34","0:36","0:40","0:48","1:01","1:02","1:04","1:08","1:16","1:32","2:01","2:02","2:04","2:08","2:16","2:32","3:00","4:01","4:02","4:04","4:08","4:16","4:32","5:00","6:00","8:01","8:02","8:04","8:08","8:16","8:32","9:00","10:00"]:
        assert False, a
