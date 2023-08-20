from typing import List

class Solution:
    def missingNumber(self, nums: List[int], left: int=0, right: int=0) -> int:
        if not nums:
            return 
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] != mid:
                right = mid - 1
            else:
                left = mid + 1
        return left