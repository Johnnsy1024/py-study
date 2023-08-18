"""
给定一个n*m的二维数组，每行每列都是从左往右从上到下的递增，给定target，查找是否有target
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
"""
class Solution:
    def find_target(self, matrxi: list, target: int):
        n, m = len(matrxi), len(matrxi[0])
        row, col = 0, m - 1
        while row < n and col >=0:
            if matrxi[row][col] > target:
                col -= 1
            elif matrxi[row][col] < target:
                row += 1
            else:
                return True
        return False

s = Solution()
matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
target = 5
print(s.find_target(matrix, target))

"""时间复杂度为O(m+n)，空间复杂度为O(1)"""