from typing import List
"""
该题重点在于动态规划和无后效性
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 
        if n == 1:
            return nums[0]
        dp = [0] * n
        dp[0] = nums[0] # dp[i]表示以nums[i]结尾的最大连续子数组
        for i in range(1, n):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
        return max(dp)
    
class Solution: # 针对上面的优化版
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 
        if n == 1:
            return nums[0]
        pre = nums[0]
        glo = pre
        for i in range(1, n):
            tmp = max(pre + nums[i], nums[i])
            pre = tmp
            glo = max(glo, pre)
        return glo

s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

        
