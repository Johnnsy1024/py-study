from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        cnt = 0
        mid = len(nums) // 2
        if nums[mid] > target:
            cnt += self.search(nums[:mid], target)
        elif nums[mid] < target:
            cnt += self.search(nums[mid+1:], target)
        else:
            cnt += 1
            cnt += self.search(nums[:mid], target)
            cnt += self.search(nums[mid+1:], target)
        return cnt