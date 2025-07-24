class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_c = Counter(s)
        for i, t in enumerate(s):
            if s_c[t] == 1:
                return i
        return -1
                