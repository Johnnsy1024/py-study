"""
双指针：找到一个有序数组中两数和为target的对应两个下表
"""

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers:
            return -1
        left, right = 0, len(numbers) - 1
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left+1, right+1]
            elif sum < target:
                left += 1
            else:
                right -= 1

s = Solution()
print(s.twoSum([3,24,50,79,88,150,345], 200))