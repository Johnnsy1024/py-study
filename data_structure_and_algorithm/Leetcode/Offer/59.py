from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        res = []
        q = deque()
        for i in range(len(nums)):
            #  队列中有数才会开始和当前遍历到的数值比较
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            while q and q[0] <= i - k:  # 当队首存储的下标(默认是当前窗口的最大值)已经在window的左侧时，将其弹出
                q.popleft()
            q.append(i)
            if i >= k - 1:
                res.append(nums[q[0]])
        return res

nums = [1, 3, 1, 2, 0, 5]
s = Solution()
print(s.maxSlidingWindow(nums, 3))