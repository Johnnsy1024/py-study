import numpy as np
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mat = []
        for _ in range(m):
            if _ == 0:
                mat.append([1] * n)
            else:
                mat.append([1] + [0] * (n - 1))
        for i in range(1, m):
            for j in range(1, n):
                mat[i][j] = mat[i - 1][j] + mat[i][j - 1]
        return np.array(mat)

s = Solution()
print(s.uniquePaths(3, 7))