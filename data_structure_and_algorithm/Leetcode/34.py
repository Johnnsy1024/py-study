"""
给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回 [-1, -1]
"""
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