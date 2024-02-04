# 地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？



# 深度优先
# class Solution:
#     def movingCount(self, m: int, n: int, k: int) -> int:
#         def judge(num1, num2, k):
#             res = 0
#             while num1:
#                 res += num1 % 10
#                 num1 = num1 // 10
#             while num2:
#                 res += num2 % 10
#                 num2 = num2 // 10
#             return res <= k
#         direction = {(-1, 0), (1, 0), (0, 1), (0, -1)}
#         used = set()
#         def dfs(x, y, used: set):
#             if x < 0 or x >= m or y < 0 or y >= n:
#                 return 0
#             if not judge(x, y, k):
#                 return 0
#             if (x, y) in used:
#                 return 0
#             used.add((x, y))
#             cnt = 1
#             for i, j in direction:
#                 cnt += dfs(x+i, y+j, used)
#             return cnt
#         return dfs(0,0,used)
# 广度优先
from collections import deque
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def judge(num1, num2, k):
            res = 0
            while num1:
                res += num1 % 10
                num1 = num1 // 10
            while num2:
                res += num2 % 10
                num2 = num2 // 10
            return res <= k
        direction = {(-1, 0), (1, 0), (0, 1), (0, -1)}
        used = set()
        # used.add((0, 0))
        def bfs(x, y, used: set):
            if x < 0 or x >= m or y < 0 or y >= n:
                return 0
            if not judge(x, y, k):
                return 0
            if (x, y) in used:
                return 0
            q = deque()
            q.append((x, y))
            used.add((x, y))
            cnt = 1
            while q:
                x, y = q.popleft()
                # if x < 0 or x >= m or y < 0 or y >= n or not judge(x, y, k) or (x, y) in used:
                #     continue
                # used.add((x, y))
                # cnt += 1
                for i, j in direction:
                    if x+i < 0 or x+i >= m or y+j < 0 or y+j >= n or not judge(x+i, y+j, k) or (x+i, y+j) in used:
                        continue
                    q.append((x+i, y+j))
                    used.add((x+i, y+j))
                    cnt += 1
            return cnt
        res = bfs(0, 0, used)
        return res
s = Solution()
print(s.movingCount(2, 3, 1))