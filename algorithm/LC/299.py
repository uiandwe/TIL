class Solution:
    def wordPattern(self, pattern: str, str1) -> bool:
        strs = str1.split(" ")
        d = {}

        if len(pattern) != len(strs):
            return False

        for index, p in enumerate(pattern):
            s = strs[index]
            if p+"_p" in d.keys():
                if d[p+"_p"] == s and s in d.keys() and d[s] == p:
                    continue
                else:
                    return False
            else:
                if s in d.keys():
                    return False
                d[s] = p
                d[p+"_p"] = s
        return True




s = Solution()
assert s.wordPattern("abba", "dog cat cat dog") is True
assert s.wordPattern("abba", "dog dog dog dog") is False
assert s.wordPattern("abba", "dog cat cat fish") is False
assert s.wordPattern("abc", "b c a") is True
assert s.wordPattern("ab", "dog dog") is False
