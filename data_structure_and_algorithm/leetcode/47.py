"""
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
"""
from typing import List

class Solution:
    def backtrack(self, path, used_idx, result, nums):
        if len(path) == len(nums):
            result.append(path[:])
            return
        used = []
        for i in range(len(nums)):
            if i not in used_idx and nums[i] not in used:
                used_idx.append(i)
                used.append(nums[i])
                path.append(nums[i])
                self.backtrack(path, used_idx, result, nums)
                path.pop()
                used_idx.pop()

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.backtrack([], [], result, nums)
        return result

s = Solution()
nums = [4, 4, 4]
print(s.permuteUnique(nums))


