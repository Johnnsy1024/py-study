"""
我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number)
求按从小到大的顺序的第 n 个丑数
"""
import heapq

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap, res = [], []
        heapq.heappush(heap, 1)
        record = set()
        for i in range(n):
            min_val = heapq.heappop(heap)
            heapq.heap
            record.add(min_val * 2)
            record.add(min_val * 3)
            record.add(min_val * 5)
            heapq.heappush()
            res.append(min_val)