from typing import List

class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] % 2 == 0 and nums[r] % 2 != 0:
                nums[l], nums[r] = nums[r], nums[l]
            elif nums[l] % 2 == 0:
                r -= 1
            elif nums[r] % 2 != 0:
                l += 1
            else:
                r -= 1
                l += 1
        return nums
    
s = Solution()
print(s.exchange([2, 6, 7, 5, 1]))