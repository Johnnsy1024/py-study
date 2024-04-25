from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left, right = 0, len(nums) - 1
        while left <= right:
            middle = left + (right - left) // 2
            if target > nums[middle]:
                left = middle + 1
            if target < nums[middle]:
                right = middle - 1
            if target == nums[middle]:
                return middle
        return -1 

s = Solution()
print(s.search([-1,0,3,5,9,12], 9))