class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'
        count = sum(1 for char in s[:k] if char in vowels)
        max_count = count
        for i in range (k,len(s)):
            if s[i] in vowels:
                count += 1
            if s[i-k] in vowels:
                count -= 1
            max_count = max(max_count, count)
        
        return max_count

