class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            ch = set()
            for j in range(i, len(s)):
                if s[j] in ch:
                    break
                ch.add(s[j])
            res = max(res, len(ch))
        return res