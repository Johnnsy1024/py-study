"""
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。

不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
"""

class Solution:
    def removeElement(self, nums, val: int) -> int:
        if not nums:
            return 
        s, f = 0, 0

        while f < len(nums):
            if nums[f] != val:
                nums[s] = nums[f]
                s += 1
                f += 1
            else:
                f += 1

        return s
    
    
s = Solution()
print(s.removeElement([0,1,2,2,3,0,4,2], 3))