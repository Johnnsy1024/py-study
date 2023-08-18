class Solution:
    def extend_left_right(self, left, right, s: str):
        cnt = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            cnt += 1
            left -= 1
            right += 1
        return s[left + 1: right], cnt
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            _, num1 = self.extend_left_right(i, i, s)
            _, num2 = self.extend_left_right(i, i+1, s)
            count += num1
            count += num2
        return count
    
s = Solution()
print(s.countSubstrings('aaa'))