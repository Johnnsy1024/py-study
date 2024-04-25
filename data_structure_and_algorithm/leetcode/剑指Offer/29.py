"""
输入一个矩阵，按从外到内顺时针的顺序依次打印每一个数字
"""
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        l, r, t, b, res = 0, len(matrix[0]) - 1, 0, len(matrix) - 1, []
        while 1:
            for i in range(l, r+1):
                res.append(matrix[t][i])
            t += 1
            if t > b:
                break
            for i in range(t, b+1):
                res.append(matrix[i][r])
            r -= 1
            if r < l:
                break
            for i in range(r, l-1, -1):
                res.append(matrix[b][i])
            b -= 1
            if b < t:
                break
            for i in range(b, t-1, -1):
                res.append(matrix[i][l])
            l += 1
            if l > r:
                break
        return res