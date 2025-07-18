class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        diff = 0
        if nums[0] < 0:
            diff = -nums[0]
    
        for i in range(len(nums)-1):
            left = i
            for j in range(len(nums)-2):
                right = len(nums) - j -1
                l_mid, r_mid = left+1, right-1
                while l_mid < r_mid:
                    s = nums[left] + nums[right] + nums[l_mid] + nums[r_mid] 
                    if s > target :
                        r_mid -= 1 
                    elif s < target :
                        l_mid += 1
                    else:
                        quad = [nums[left] ,nums[l_mid], nums[r_mid], nums[right]]
                        if len(result)== 0 or (len(result) > 0 and quad not in result):
                            result.append(quad)
                        l_mid += 1
                        r_mid -= 1
        return result

