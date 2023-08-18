class Solution:
    def cuttingRope(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[2] = 1
        for i in range(3, n + 1):
            """
            假设一条长为i的绳子，如果一段被拆成1，另一段为i-1的话，则这个操作不会对结果带来任何好处
            所以从2开始
            """
            for j in range(2, i):
                # 内层max中第一项：如果分成j和i-j，i-j不接着分的结果
                # 内层max中第二项：如果分成j和i-j，i-j接着去分
                tmp1 = j * (i - j)
                tmp2 = j * dp[i - j]
                dp[i] = max(dp[i], max(tmp1, tmp2))
        return dp[n]


s = Solution()
res = s.cuttingRope(10)
