"""
我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number)
求按从小到大的顺序的第 n 个丑数
"""
import heapq

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        res = 1
        if n == 1:
            return res
        heap, tmp = [1], set([1])
        for i in range(2, n+2):
            min_val = heapq.heappop(heap)
            if min_val * 2 not in tmp:
                tmp.add(min_val * 2)
                heapq.heappush(heap, min_val * 2)
            if min_val * 3 not in tmp:
                tmp.add(min_val * 3)
                heapq.heappush(heap, min_val * 3)
            if min_val * 5 not in tmp:
                tmp.add(min_val * 5)
                heapq.heappush(heap, min_val * 5)
        return min_val
# import heapq

# class Solution:
#     def nthUglyNumber(self, n: int) -> int:
#         if n == 1:
#             return 1
#         heap = [1]
#         seen = {1}
#         primes = [2, 3, 5]
        
#         for _ in range(n - 1):
#             current = heapq.heappop(heap)
#             for prime in primes:
#                 next_ugly = current * prime
#                 if next_ugly not in seen:
#                     seen.add(next_ugly)
#                     heapq.heappush(heap, next_ugly)
        
#         return heapq.heappop(heap)

# 示例用法
solution = Solution()
print(solution.nthUglyNumber(10))  # 输出 12

# s = Solution()
# print(s.nthUglyNumber(10))