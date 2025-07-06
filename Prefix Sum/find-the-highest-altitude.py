class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_h = 0
        prefix = 0
        for i in range (len(gain)):
            prefix += gain[i]
            max_h = max(max_h, prefix)

        return max_h