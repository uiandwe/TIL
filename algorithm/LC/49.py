class Solution:
    def groupAnagrams(self, strs):
        d = {}

        for c in strs:
            temp = ''.join(sorted(c))
            if temp in d:
                d[temp].append(c)
            else:
                d[temp] = [c]

        return list(d.values())


s = Solution()
s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
