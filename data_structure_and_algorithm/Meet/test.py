from collections import deque
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        def bfs(start_i, start_j, used : set):
            # 初始的(start_i, start_j)一定是一个"1"
            res = []
            q = deque([(start_i, start_j)])
            if grid[start_i][start_j] == '1':
                res.append((start_i, start_j))
            else:
                return
            while q:
                i, j = q.popleft()
                for add_i, add_j in dire:
                    n_i, n_j = i + add_i, j + add_j
                    if m > n_i >=0 and n > n_j >= 0 and (n_i, n_j) not in used\
                        and (n_i, n_j) not in q and grid[n_i][n_j] == '1':
                        q.append((n_i, n_j))
                        res.append((n_i, n_j))
                        used.add((n_i, n_j))
            return res
        res = 0
        i, j = 0, 0
        dire = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m = len(grid)
        n = len(grid[0])
        used = set()
        cnt = 0
        result = []
        while i < m:
            while j < n:
                if (i, j) not in used and grid[i][j] == '1':
                    result.append(bfs(i, j, used))
                    cnt += 1
                j += 1
            i += 1
            j = 0
        return cnt

s = Solution()
grid = [["1","1","0","0","0"], ["1","1","0","0","0"], ["0","0","1","0","0"], ["0","0","0","1","1"]]
print(s.numIslands(grid))
# m = len(grid)
# n = len(grid[0])
# def bfs(start_i, start_j, used : set):
#     dire = [(1, 0), (-1, 0), (0, 1), (0, -1)]
#     res = []
#     q = deque([(start_i, start_j)])
#     if grid[start_i][start_j] == '1':
#         res.append((start_i, start_j))
#     while q:
#         i, j = q.popleft()
#         for add_i, add_j in dire:
#             n_i, n_j = i + add_i, j + add_j
#             if m > n_i >=0 and n > n_j >= 0 and (n_i, n_j) not in used\
#                 and (n_i, n_j) not in q and grid[n_i][n_j] == '1':
#                 q.append((n_i, n_j))
#                 res.append((n_i, n_j))
#                 used.add((n_i, n_j))
#     return res, used

# print(bfs(0, 2, set()))