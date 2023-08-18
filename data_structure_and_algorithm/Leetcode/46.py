"""
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。
"""
from typing import List

class Solution:
    def backtrack1(self, nums, path: list, idx_list : list, result):
        if len(path) == len(nums):
            result.append(path.copy())  # 注意这里不能直接append path本身，否则会传递引用进去
            return
        
        for idx, num in enumerate(nums):
            if idx not in idx_list:
                path.append(num)
                idx_list.append(idx)
                self.backtrack1(nums, path, idx_list, result)
                path.pop()
                idx_list.pop()

    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.backtrack1(nums, [], [], result)
        return result
    