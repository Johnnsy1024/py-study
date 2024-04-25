def minPathSum(matrix):
    m = len(matrix)
    n = len(matrix[0])

    dp = [[0] * n for _ in range(m)]
    dp[0][0] = matrix[0][0]

    # 初始化第一行
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + matrix[0][j]

    # 初始化第一列
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + matrix[i][0]

    # 计算其他位置的最短路径和
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + matrix[i][j]

    return dp[m-1][n-1]
