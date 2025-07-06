class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                # Check skipping left
                i, j = left + 1, right
                while i < j and s[i] == s[j]:
                    i += 1
                    j -= 1
                if i >= j:
                    return True

                # Check skipping right
                i, j = left, right - 1
                while i < j and s[i] == s[j]:
                    i += 1
                    j -= 1
                return i >= j

            left += 1
            right -= 1

        return True
