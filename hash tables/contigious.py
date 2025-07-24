class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        if len(nums) / 2 == sum(nums):
            return len(nums)
        max_count = 0
        count_map = {0: -1}
        count = 0

        for i in range(len(nums)):
            count = count + 1 if nums[i] else  count - 1
            if count  not in count_map:
                count_map[count] = i
            else:
                if i - count_map[count] > max_count:
                    max_count =  i - count_map[count]


        return max_count