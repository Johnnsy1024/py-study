class Solution:
    def fib(self, n: int) -> int:
        dp_array = [0,1]
        if n <= 1:
            return dp_array[n]
        for i in range(2,n+1):
            dp_array.append(dp_array[i-1]+dp_array[i-2])
        return self.fib(n-1) + self.fib(n-2)

s = Solution()
print(s.fib(3))