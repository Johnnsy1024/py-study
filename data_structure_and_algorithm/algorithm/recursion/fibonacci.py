"""生成斐波那契数列有两种可能的要求：
1.输入参数n为生成数字的个数
2.输入参数n为在数字n前的斐波那契数"""

#  2
class Solution2:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fib(n - 1) + self.fib(n - 2)
#  1
class Solution1:
    def fib(self, n : list) -> int:
        res = [0, 1]
        if n <= 2:
            return res
        while len(res) < n:
            i, j = res[-2], res[-1]
            res.append(i+j)
        return res
s = Solution1()
print(s.fib(15))
