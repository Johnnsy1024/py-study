from typing import List
from collections import deque
"""
本题的逻辑如下：未挖出的方块应该持续递归地被挖出，而递归中止的条件即为从当前点击位置后所有显示数字（与地雷相邻）的格子都被找出来
而且要注意，是从初始位置点击一次，而不是一直把所有的地雷都找出来
"""
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        i, j = click
        if board[i][j] == 'M':
            board[i][j] = 'X'
            return board
        
        row_num, col_num = len(board), len(board[0])

        def cal_num(i, j):
            res = 0
            for x in [-1, 1, 0]:
                for y in [-1, 1, 0]:
                    if x == 0 and y == 0:
                        continue
                    next_i, next_j = i + x, j + y
                    if 0 <= next_i < row_num and 0 <= next_j < col_num and board[next_i][next_j] == 'M':
                        res += 1
            return res


        def bfs(i, j):
            q = deque()
            q.append([i, j]) # 这里可以保证起点一定不是地雷点
            while q:
                i, j = q.popleft()
                cnt = cal_num(i, j)
                if cnt > 0:
                    board[i][j] = str(cnt)
                    continue # 如果队列中没有
                board[i][j] = 'B'
                for x in [1, -1, 0]:
                    for y in [1, -1, 0]:
                        if x == 0 and y == 0:
                            continue
                        if i+x < 0 or i+x >= row_num or j+y < 0 or j+y >= col_num:
                            continue
                        if board[i+x][j+y] == 'E':
                            q.append([i+x, j+y])
                            board[i+x][j+y] = 'B'

        bfs(i,j)
        return board
    
board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]]
click = [3,0]
s = Solution()
print(s.updateBoard(board=board, click=click))