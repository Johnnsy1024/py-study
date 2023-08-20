"""
给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
"""
from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row_num = len(board)
        col_num = len(board[0])

        def dfs(x, y, index):
            # 从当前(x,y)位置深度优先搜索，是否能够搜出对应的word
            if index == len(word):
                return True
            for dx, dy in {(-1, 0), (1, 0), (0, -1), (0, 1)}:
                nx, ny = x + dx, y + dy
                if 0 <= nx < row_num and 0 <= ny < col_num and board[nx][ny] == word[index]:
                    board[nx][ny] = '*'
                    if dfs(nx, ny, index+1):
                        return True
                    board[nx][ny] = word[index]
            # 如果遍历了所有的四个方向的深度优先搜索都搜不出来，及时止损（剪枝）
            return False

        for m in range(row_num):
            for n in range(col_num):
                if board[m][n] == word[0]:
                    board[m][n] = '*'
                    if dfs(m, n, 1):
                        return True
                    board[m][n] = word[0] # 这里强调一下dfs为什么一定要有“恢复原样”这一步，如果当前这组(m,n)没有搜索到，那么可能还需要其他组的(m, n)来搜索
        return False

                
