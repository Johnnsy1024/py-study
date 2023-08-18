import math

class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        left, right = 1, x
        while left <= right:
            mid = left + (right - left) // 2
            if mid ** 2 == x:
                return mid
            if mid ** 2 > x:
                right = mid - 1
            elif mid ** 2 == x:
                return int(mid)
            elif math.ceil(mid)**2 == x:
                return math.ceil(mid)
            elif mid ** 2 < x and math.ceil(mid)**2 > x:
                return math.floor(mid)
            else:
                left = mid