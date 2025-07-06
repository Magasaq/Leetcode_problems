class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        word = set()
        max_str = 0
        for right in range(len(s)):
            while s[right] in word:
                word.remove(s[left])
                left += 1
            word.add(s[right])
            max_str = max(max_str, right - left + 1)
        return max_str
