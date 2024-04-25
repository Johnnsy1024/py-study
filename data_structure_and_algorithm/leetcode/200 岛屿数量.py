from typing import List
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        def bfs(start_i, start_j, used: set):
            q = deque([(start_i, start_j)])
            while q:
                i, j = q.popleft()
                for add_i, add_j in dire:
                    n_i, n_j = i + add_i, j + add_j
                    if 0 <= n_i < m and 0 <= n_j < n and (n_i, n_j) not in used \
                            and grid[n_i][n_j] == '1':
                        q.append((n_i, n_j))
                        used.add((n_i, n_j))
            return res

        res = 0
        dire = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m = len(grid)
        n = len(grid[0])
        used = set()

        for i in range(m):
            for j in range(n):
                if (i, j) not in used and grid[i][j] == '1':
                    bfs(i, j, used)
                    res += 1

        return res


# 更优方法
# class Solution:
#     def numsIslands(self, grid: List[List[str]]) -> int:
#         m = len(grid)
#         n = len(grid[0])
#         res = 0
#
#         def dfs(x, y):
#             if grid[x][y] == '1':
#                 grid[x][y] = 0
#             else:
#                 return
#             if x > 0:
#                 dfs(x - 1, y)
#             if x < m - 1:
#                 dfs(x + 1, y)
#             if y > 0:
#                 dfs(x, y - 1)
#             if y < n - 1:
#                 dfs(x, y + 1)
#
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == "1":
#                     dfs(i, j)
#                     res += 1
#         return res


s = Solution()
grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
print(s.numIslands(grid))
