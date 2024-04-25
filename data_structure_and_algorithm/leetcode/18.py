from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            return []
        nums.sort()
        res = []
        for a in range(len(nums)-3):
            # 跳过重复数字
            if a and nums[a] == nums[a - 1]:
                continue
            if nums[a] + nums[a+1] + nums[a+2] + nums[a+3] > target:
                break
            if nums[a] + nums[-1] + nums[-2] + nums[-3] < target:
                continue
            for b in range(a + 1, len(nums) - 2):
                if b > a + 1 and nums[b] == nums[b - 1]:
                    continue
                c = b + 1
                d = len(nums) - 1
                while c < d:
                    tmp = nums[a] + nums[b] + nums[c] + nums[d]
                    if tmp < target:
                        c += 1
                    if tmp > target:
                        d -= 1
                    if tmp == target:
                        res.append([nums[a],nums[b],nums[c],nums[d]])
                        while c < d and nums[c] == nums[c+1]:
                            c += 1
                        while c < d and nums[d] == nums[d-1]:
                            d -= 1
                        c += 1
                        d -= 1
        
        return res

s = Solution()
nums = [2,2,2,2,2]
print(s.fourSum(nums, 8))