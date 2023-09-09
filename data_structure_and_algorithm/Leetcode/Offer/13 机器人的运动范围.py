"""
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，
它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。
例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。
请问该机器人能够到达多少个格子？
"""
def divide(num):
    res = 0
    while num > 0:
        res += num % 10
        num = num // 10
    return res

direction = {(-1, 0), (1, 0), (0, 1), (0, -1)}

def func(m, n, k):
    cnt = 0
    used = set()

    def dfs(x, y, used):
        if x < 0 or x >= m or y < 0 or y >= n:
            # Cell is out of bounds, terminate the recursion
            return 0
        if divide(x) + divide(y) > k:
            # Cell doesn't satisfy the condition, terminate the recursion
            return 0
        if (x, y) in used:
            # Cell has already been visited, terminate the recursion
            return 0

        nonlocal cnt  # Use the cnt variable from the outer function
        cnt += 1  # Count this cell as visited
        used.add((x, y))

        for i, j in direction:
            cnt += dfs(x + i, y + j, used)

        used.discard((x, y))
        return cnt

    return dfs(0, 0, used)

m = 3
n = 2
k = 17
print(func(m, n, k))
