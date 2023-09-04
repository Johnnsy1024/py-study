from typing import List
from collections import deque

# 用双端队列（超时）
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        q = deque([nums[0]])
        i = 1
        min_len = float('inf')
        while q:
            if sum(q) < target and i < len(nums):
                q.append(nums[i])
                i += 1
            if sum(q) < target and i >= len(nums):
                q.popleft()
            if sum(q) >= target:
                min_len = min(min_len, len(q))
                q.popleft()
        if min_len == float('inf'):
            return 0
        else:
            return min_len

# 用快慢指针
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, 0
        tmp = 0
        res = float('inf')
        while right < len(nums):
            tmp += nums[right]
            while tmp >= target:
                res = min(res, right - left + 1)
                tmp -= nums[left]
                left += 1
            right += 1
        return res if res!= float('inf') else 0
s = Solution()
target = 4
nums = [1,4,4]
print(s.minSubArrayLen(target, nums))