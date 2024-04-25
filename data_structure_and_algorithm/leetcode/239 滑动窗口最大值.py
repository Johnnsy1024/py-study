from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) <= 1:
            return nums
        n = len(nums)
        q = deque()
        res = []
        for i in range(n):
            while q and nums[i] > nums[q[-1]]:
                q.pop()
            q.append(i)
            while q and i - q[0] + 1 > k:
                q.popleft()
            if i + 1 - k >= 0:
                res.append(nums[q[0]])
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))