class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        set_n = set(nums)
        for s in set_n:
            if nums.count(s) > len(nums)//2:
                return s

