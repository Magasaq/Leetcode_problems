class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_prefix = 0
        prefix = 0

        for i in range(len(nums)):
            prefix += nums[i]
            min_prefix = min(min_prefix, prefix)

        return max(1-min_prefix, 0)