"""
从m个种类的球中买n个，第一个种类至少买一个，返回总的方案数
思路：动态规划：dp[n][m] = dp[n][m-1] + k
k = dp[n-1][m]
k代表球种类由m-1增加到m后取球的方法增加数量，其等于在买n个球的策略中至少买一个第m类球的策略数量，也就是单独空出一个位置专买第m类，这样的话等于dp[n-1][m]
"""


def select(n: int, m: int):
    dp = [[0] * m for _ in range(n)]
    for i in range(m):
        dp[0][i] = 1
    for j in range(n):
        dp[j][0] = 1
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = dp[i][j-1] + dp[i-1][j]
    return dp[n-1][m-1]

print(select(4, 4))