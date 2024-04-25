"""
给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回 [-1, -1]
"""
from typing import List
# 方法1：普通二分查找找到一个target后，以这个target所在位置为初始位置向两侧延伸（延伸条件为不过界且指针所指元素依然等于target）
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]: 
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                left_idx = right_idx = mid
                while left_idx > 0 and nums[left_idx] == nums[left_idx - 1]:
                    left_idx -= 1
                while right_idx < len(nums) - 1 and nums[right_idx] == nums[right_idx + 1]:
                    right_idx += 1
                return [left_idx, right_idx]
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return [-1, -1]   
# 方法2：两轮二分查找，第一轮找到最左侧的（right不断减小），第二轮找到最右侧的（left不断增大）
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]: 
        first, last = -1, -1
        if not nums:
            return [first, last]
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            # 先找到大于等于target的值
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                first = mid
                right = mid - 1
        left, right = first, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            # 先找到大于等于target的值
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                second = mid
                left = mid + 1
        return [first, second]  

s = Solution()
print(s.searchRange([5,7,7,8,8,10], 8))